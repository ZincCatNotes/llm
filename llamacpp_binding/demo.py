from llama_cpp import Llama
from dotenv import load_dotenv
import os

load_dotenv(".env")
env_dist = os.environ
model_path = env_dist.get("MODEL_PATH")

llm = Llama(
    model_path=model_path,
    verbose=False,
)
output = llm(
    """You are a friendly assistant.
    User: Who are you?
    Assistant: """,
    max_tokens=80,
    stop=["User:", "\n"],
    echo=False,
)
print(output)
