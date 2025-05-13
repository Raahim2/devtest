from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://huggingface.co/api/inference-proxy/together",
    api_key="mai nahi bataunga"
)

def n():
    pass

def deepseek(prompt):
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    stream = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1", 
        messages=messages, 
        max_tokens=500,
        stream=True
    )

    response = ""
    for chunk in stream:
        if chunk.choices:
            response += chunk.choices[0].delta.content
    return response

@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    user_input = None
    if request.method == 'POST':
        user_input = request.form['prompt']
        response = deepseek(user_input)
    return render_template('index.html', response=response, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
