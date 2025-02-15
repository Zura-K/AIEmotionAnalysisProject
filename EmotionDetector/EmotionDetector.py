import requests
import json


class EmotionDetector:
    def __init__(self):
        self.url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        self.headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    def emotion_detector(self, text_to_analyze):
        payload = {"raw_document": {"text": text_to_analyze}}

        try:
            response = requests.post(self.url, headers=self.headers, json=payload, timeout=15)
            response.raise_for_status()
            data = response.json()

            emotion_predictions = data.get("emotionPredictions", [])
            if not emotion_predictions:
                return {"error": "No emotion predictions found in response."}

            emotions = emotion_predictions[0].get("emotion", {})
            if not emotions or not isinstance(emotions, dict):
                return {"error": "No emotions detected."}

            return self.format_response(emotions)

        except requests.exceptions.Timeout:
            return {"error": "Request timed out. Try again later."}
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}

    @staticmethod
    def format_response(emotions):
        if not emotions or not isinstance(emotions, dict):
            return {"error": "No emotions detected"}

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': emotions.get('anger', 0.0),
            'disgust': emotions.get('disgust', 0.0),
            'fear': emotions.get('fear', 0.0),
            'joy': emotions.get('joy', 0.0),
            'sadness': emotions.get('sadness', 0.0),
            'dominant_emotion': dominant_emotion
        }