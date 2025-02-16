"""
Flask server for emotion detection application.
Handles API requests and renders web interface.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetector.EmotionDetector import EmotionDetector

class Server:
    """Server class to handle emotion detection API and web interface."""

    def __init__(self):
        """Initialize the Flask app and set up routes."""
        self.app = Flask(__name__)
        self.detector = EmotionDetector()
        self.setup_routes()

    def setup_routes(self):
        """Define API and web routes for the Flask app."""

        @self.app.route('/emotionDetector', methods=['GET', 'POST'])
        def emotion_detector():
            """
            Handles emotion detection requests via GET and POST methods.

            Returns:
                JSON: Emotion analysis or error message.
            """
            if request.method == 'GET':
                text_to_analyze = request.args.get("textToAnalyze", "")
                response_code = int(request.args.get("status_code", 200))
            else:
                data = request.get_json()
                text_to_analyze = data.get("text", "")
                response_code = int(data.get("status_code", 200))

            if response_code == 400 or not text_to_analyze.strip():
                return jsonify({"response": "Invalid text! Please try again!"}), 400

            result = self.detector.emotion_detector(text_to_analyze)

            if not result or result.get("dominant_emotion") is None:
                return jsonify({"response": "Invalid text! Please try again!"}), 400

            response_text = "For the given statement, the system response is "
            response_text += ", ".join(
                [f"{key}: {value}" for key, value in result.items()
                 if key != 'dominant_emotion']
            )
            response_text += f". The dominant emotion is {result['dominant_emotion']}."

            return jsonify({"response": response_text})

        @self.app.route('/')
        def home():
            """
            Renders the home page.

            Returns:
                HTML: The rendered index page.
            """
            return render_template('index.html')

    def run(self):
        """
        Runs the Flask application.

        Starts the Flask app on port 5000.
        """
        self.app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    server = Server()
    server.run()
