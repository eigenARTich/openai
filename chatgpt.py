import openai

API_KEY = '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'

def chat(prompt):
    completions = openai.Completion.create(model='text-davinci-002', prompt=prompt, max_tokens=1024, api_key=API_KEY)
    message = completions.choices[0].text
    return message

result = chat('Erkläre Bitcoin einem Kind')
print(result)




