import json
import os
import pandas as pd

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

NEBULA_BASE_URL = 'http://localhost/api/'
NEBULA_API_KEY = os.getenv('NEBULA_API_KEY')
NEBULA = OpenAI(base_url=NEBULA_BASE_URL, api_key=NEBULA_API_KEY)


EXPERIMENT = 'baseline'
MODELS_DICT = {
    'large': {
        'gemma': 'gemmalarge',
        'ds': 'dslarge'
    }, 
    'small': {
        'gemma': '',
        'ds': ''
    }, 

}

QUESTIONS_DICT = {
    'large': ['My traces don’t appear in Grafana. How can I fix this?',
              'How should I choose a HTTPS solution?',
              'Explain the log levels.',
              'What are the Workspace permissions?',
              'I need a compose yml that integrates watchtower',
              'What is the Open WebUI license in full? Cite it.', 
              'What are all the environment variables? Give me a list.'],
    'small': ['']
}


def prompt_nebula(model, user_prompt):
    prompt_parameters = {
        "model": model,
        "messages": [
            { "role": "user", "content": user_prompt }
        ],
    }

    response = NEBULA.chat.completions.create(**prompt_parameters)
    return response


def usage_to_df(usage):
    columns = [key[0] for key in usage]
    row = [[key[1] for key in usage]]
    return pd.DataFrame(row, columns=columns)



if __name__=='__main__':
    cols=['model', 'question', 'response', 'completion_tokens', 'prompt_tokens', 'total_tokens', 'completion_tokens_details', 'prompt_tokens_details', 'response_token/s', 'prompt_token/s', 'total_duration', 'load_duration', 'prompt_eval_count', 'prompt_eval_duration', 'eval_count', 'eval_duration', 'approximate_total']
    df = pd.DataFrame(columns=cols)
    print(df.columns)

    kb_size = 'large'
    model = 'ds'


    response = prompt_nebula(MODELS_DICT[kb_size][model], QUESTIONS_DICT[kb_size][4])
    # print(f"Response: {response.choices[0].message.content}\n\n")
    print(f"Response: {response}")
    with open(f'{EXPERIMENT}/{model}_{str(question)}.log', 'w') as writer:
        writer.write(response)
    print(100*"-")

    print(usage_to_df(response.usage))

