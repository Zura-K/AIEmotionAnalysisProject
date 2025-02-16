from flask import Flask, request, jsonify, render_template
from EmotionDetector.EmotionDetector import EmotionDetector

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.detector = EmotionDetector()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/emotionDetector', methods=['GET', 'POST'])
        def emotion_detector():
            if request.method == 'GET':
                text_to_analyze = request.args.get("textToAnalyze", "")
            else:
                data = request.get_json()
                text_to_analyze = data.get("text", "")

            if not text_to_analyze:
                return jsonify({"error": "No text provided"}), 400

            result = self.detector.emotion_detector(text_to_analyze)
            text = "For the given statement, the system response is"
            for key, emotion in result:
                if key != 'dominant_emotion':
                    text += key + ":" + emotion
            text += "The dominant emotion is {result['dominant_emotion']}."
            response_text = (
                text
            )

            return jsonify({"response": response_text})

        @self.app.route('/')
        def home():
            return render_template('index.html')

    def run(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    server = Server()
    server.run()
