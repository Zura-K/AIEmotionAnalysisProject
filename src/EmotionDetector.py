import requests

class EmotionDetector:
    def __init__(self):
        self.url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        self.headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    def emotion_detector(self, text_to_analyze):
        payload = {"raw_document": {"text": text_to_analyze}}
        response = requests.post(self.url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch emotion analysis"}
