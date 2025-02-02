from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='hf.co/mmnga/cyberagent-DeepSeek-R1-Distill-Qwen-32B-Japanese-gguf:Q4_K_M', messages=[
  {
    'role': 'user',
    'content': '空が青いのは何故ですか？',
  },
])

print(response['message']['content'])