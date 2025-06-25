import requests
from pprint import pprint
import uuid

url = "https://n8n.kisrv.com/webhook/5a2f8cd9-d16c-439f-918e-7b76a80a4bd1"

def get_chat(user_id, chat_input):
    # Generate a unique UUID for this chat
    chat_id = str(uuid.uuid4())

    # Prepare payload with both chat input and UUID
    payload = {
        "userId": user_id,
        "chatInput": chat_input,
        "chatId": chat_id
    }

    response = requests.post(url, json=payload)
    data = response.json()

    # Optionally, attach the UUID to the response for tracking
    data["chatId"] = chat_id

    return data

# # Example usage
# res = get_chat("user_123", "what does it do?")
# pprint(res)
