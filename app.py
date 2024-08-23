from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key
api_key = ''

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Get text and target language from the request
        text = request.json.get('text')
        target_language = request.json.get('target_language')

        # Perform the translation request
        response = requests.post(
            'https://translation.googleapis.com/language/translate/v2',
            params={'key': api_key},
            json={'q': text, 'target': target_language, 'format': 'text'}
        )

        # Parse the JSON response
        result = response.json()

        # Print the entire response for debugging
        print(result)

        # Check if 'data' is in the result before accessing it
        if 'data' in result:
            translated_text = result['data']['translations'][0]['translatedText']
            return jsonify({'translatedText': translated_text})
        else:
            # Return an error message if 'data' is not found
            return jsonify({'error': 'Translation failed', 'response': result}), 500

    except Exception as e:
        # Catch any other exceptions and return an error response
        print(f"Error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
