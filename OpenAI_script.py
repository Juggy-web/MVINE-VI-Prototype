import json
import os
import openai

def lambda_handler(event, context):
    # TODO implement
    
    
    openai.api_key = os.environ['key']

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=("The following is a casual conversation between two friends.\n\nFriend: " + event['inputTranscript'] + "\nAI: "),
        temperature=0.5,
        max_tokens=100,
        presence_penalty=0.6,
        #stop=["Friend: ","AI: "]
        )
        
    text_response = response['choices'][0]['text'].strip()
    
    return {
        "sessionState": {
            "dialogAction": {
                "type": "ElicitIntent"
            },
            "intent": {
                "confirmationState": "Confirmed",
                "name": "gpt",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": text_response
            }
        ]
        
    }