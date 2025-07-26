import openai

openai.api_key = ''  # Replace with your key or env variable

def generate_answer(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or local model if you want to use one
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()
