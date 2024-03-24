from openai import OpenAI


def generate_ai_question(text):
    client = OpenAI(api_key='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')

    response = client.chat.completions.create(
      model="gpt-4-turbo-preview",
      messages=[
        {
          "role": "system",
          "content": "Эмтихан сұрағына жауап бер"
        },
        {
          "role": "user",
          "content": text
        }
      ],
      temperature=1,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    result = ''
    if response and response.choices:
        first_choice = response.choices[0]

        if first_choice.message and first_choice.message.content:
            result = first_choice.message.content

    return result


def generate_ai_chat(text):
    client = OpenAI(api_key='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')

    response = client.chat.completions.create(
      model="gpt-4-turbo-preview",
      messages=[
        {
          "role": "system",
          "content": "Эмтихан сұрағына жауап бер"
        },
        {
          "role": "user",
          "content": text
        }
      ],
      temperature=1,
      max_tokens=500,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    result = ''
    if response and response.choices:
        first_choice = response.choices[0]

        if first_choice.message and first_choice.message.content:
            result = first_choice.message.content

    return result