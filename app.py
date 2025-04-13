from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from services.pdf_service import process_pdf
from services.query_service import run_query
from utils.helpers import allowed_file, init_directories
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf'}

# Initialize folders
init_directories([UPLOAD_FOLDER])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if not file.filename or not allowed_file(file.filename):
        return jsonify({'error': 'Invalid or missing file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        file.save(file_path)
        process_pdf(file_path)
        return jsonify({'message': 'File processed successfully'}), 200
    except Exception as e:
        print("Upload Error:", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query_text = data.get('query', '').strip()
    if not query_text:
        return jsonify({'error': 'Query text is required'}), 400

    try:
        result = run_query(query_text)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
