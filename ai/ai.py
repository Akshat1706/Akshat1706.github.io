import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a letter for leave to principle.\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
 "id": "cmpl-7VG16x4o9ngMWkNSA5SXyVtREqDaz",
  "object": "text_completion",
  "created": 1687684092,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\nDear Principal \n\nI am writing to request leave for two days, July 11th and 12th, as I need to visit my father, who is not keeping well.\n\nMy father is suffering from respiratory issues and is 
under medication. Therefore, I need to be with him for the time being.\n\nI am sure beneath your consideration and understanding, that my request will be accepted. I shall make sure to finish my work before leaving, and in my absence I will keep my teachers updated about my progress.\n\nI shall be grateful if you would allow me leave for the mentioned days.\n\nThank you for your consideration.\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 143,
    "total_tokens": 152
  }
}

'''