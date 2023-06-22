import openai
import json

api_key = "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"

def create_picture(answer_text):
    openai.api_key = api_key
    response = openai.Image.create(
        prompt=answer_text,
        n=1,
        size="256x256",
    )
    print(response)
    picture_url = response.get('data')[0].get('url')
    return picture_url

def where_to_go(preferences):
    openai.api_key = api_key
    answer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{preferences} Куда мне поехать в России?"}
        ]
    )
    answer_text = answer.get('choices')[0].get('message').get('content')
    picture_url = create_picture(answer_text)
    print(answer_text)
    print(picture_url)
    return answer_text, picture_url







