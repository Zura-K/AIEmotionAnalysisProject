import requests

class EmotionDetector:
    def __init__(self):
        self.url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        self.headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    def emotion_detector(self, text_to_analyze):
        payload = {"raw_document": {"text": text_to_analyze}}
        response = requests.post(self.url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return self.format_response(response.json())
        else:
            return {"error": "Failed to fetch emotion analysis"}

    @staticmethod
    def format_response(res):
        if not res:
            return {"error": "No emotions detected"}

        dominant_emotion = max(res, key=res.get)

        return {
            'anger': res.get('anger', 0.0),
            'disgust': res.get('disgust', 0.0),
            'fear': res.get('fear', 0.0),
            'joy': res.get('joy', 0.0),
            'sadness': res.get('sadness', 0.0),
            'dominant_emotion': dominant_emotion
        }
