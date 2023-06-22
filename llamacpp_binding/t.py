import json

# Assuming you have the corrected string data
string_data = 'data: {"id": "chatcmpl-020df3d6-e02d-4671-a4da-f8b03e506dd8", "model": "/Users/zinccat/Documents/codes/llama.cpp/models/7B/Wizard-Vicuna-7B-Uncensored.ggmlv3.q4_0.bin", "created": 1687417510, "object": "chat.completion.chunk", "choices": [{"index": 0, "delta": {"content": " x"}, "finish_reason": null}]}'

# Decoding the JSON
json_data = json.loads(string_data)

# Printing the JSON data
print(json_data)
