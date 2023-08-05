import json
import os
import openai

def lambda_handler(event, context):
    
    # Calling OPENAI API
    openai.api_key = os.environ['key']

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=(event['inputTranscript']),
        temperature=0.5,
        max_tokens=100,
        presence_penalty=0.6,
        #stop=["Friend: ","AI: "]
        )
    
    # Extracting response    
    text_response = response['choices'][0]['text'].strip()

    # Returning response to Lex
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
