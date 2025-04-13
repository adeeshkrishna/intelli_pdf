document.addEventListener('DOMContentLoaded', () => {
    const processButton = document.getElementById('processButton');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const chatSection = document.getElementById('chatSection');
    const chatBox = document.getElementById('chatBox');
    const queryInput = document.getElementById('queryInput');
    const sendButton = document.getElementById('sendButton');
    const endChatButton = document.getElementById('endChatButton');

    const appendMessage = (text, sender = 'user') => {
        const div = document.createElement('div');
        div.className = `message ${sender}`;
        div.textContent = text;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    };

    const appendSources = (sources = []) => {
        if (sources.length > 0) {
            const div = document.createElement('div');
            div.className = 'message source';
            div.textContent = `Sources: ${sources.join(', ')}`;
            chatBox.appendChild(div);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    };

    const handleUpload = async () => {
        processButton.disabled = true; // Disable button during processing
        loadingIndicator.classList.remove('hidden'); // Show spinner

        const formData = new FormData(document.getElementById('uploadForm'));
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();

            if (response.ok) {
                alert('PDFs processed successfully.');
                chatSection.classList.remove('hidden'); // Show chat section
            } else {
                appendMessage(`❌ Error: ${result.error}`, 'bot');
            }
        } catch (error) {
            appendMessage(`❌ Network error: ${error.message}`, 'bot');
        } finally {
            loadingIndicator.classList.add('hidden'); // Hide spinner
            processButton.disabled = false; // Re-enable button
        }
    };

    const handleQuery = async () => {
        const query = queryInput.value.trim();
        if (!query) return alert('Please enter a question.');

        appendMessage(query, 'user');
        queryInput.value = '';
        sendButton.disabled = true;

        try {
            const response = await fetch('/query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query })
            });
            const result = await response.json();

            if (response.ok) {
                appendMessage(result.response, 'bot');
                appendSources(result.sources);
            } else {
                appendMessage(`❌ Error: ${result.error}`, 'bot');
            }
        } catch (error) {
            appendMessage(`❌ Network error: ${error.message}`, 'bot');
        } finally {
            sendButton.disabled = false;
        }
    };

    processButton.addEventListener('click', handleUpload);
    sendButton.addEventListener('click', handleQuery);

    endChatButton.addEventListener('click', () => {
        chatBox.innerHTML = '';
        chatSection.classList.add('hidden');
        document.getElementById('uploadForm').reset(); // Reset file input
        processButton.disabled = false;
        loadingIndicator.classList.add('hidden'); // Ensure spinner is hidden when ending chat
    });    

    queryInput.addEventListener('keypress', e => {
        if (e.key === 'Enter' && !sendButton.disabled) {
            handleQuery();
        }
    });
});
