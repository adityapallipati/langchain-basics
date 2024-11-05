# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)

"""
Full result:

content='81 divided by 9 is 9.'
additional_kwargs={'refusal': None}
response_metadata={'token_usage': 
{'completion_tokens': 9, 
'prompt_tokens': 16, 
'total_tokens': 25, 
'completion_tokens_details': 
{'accepted_prediction_tokens': 0, 
'audio_tokens': None, 
'reasoning_tokens': 0, 
'rejected_prediction_tokens': 0}, 
'prompt_tokens_details': 
{'audio_tokens': None, 
'cached_tokens': 0}}, 
'model_name': 'gpt-4o-2024-08-06', 
'system_fingerprint': 'fp_159d8341cc', 
'finish_reason': 'stop', 'logprobs': None} 
id='run-dcef2bc3-137b-4c95-b559-4f2867879674-0' 
usage_metadata={'input_tokens': 16, 
'output_tokens': 9, 
'total_tokens': 25}

Content only:
81 divided by 9 is 9.

"""