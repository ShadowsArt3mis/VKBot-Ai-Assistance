# rasa_integration.py

import requests

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"  # Replace with your Rasa server URL

def get_rasa_response(message):
    """Sends a message to Rasa and returns the response."""

    payload = {"sender": "user", "message": message}

    try:
        response = requests.post(RASA_API_URL, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        response_json = response.json()
        if response_json:
            return response_json[0]['text']  # Return the first text response from Rasa
        else:
            return "I'm not sure how to respond to that."

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Rasa: {e}")
        return "Sorry, I'm having trouble connecting to the bot right now."
