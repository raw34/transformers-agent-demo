import os
from huggingface_hub import login
from transformers import HfAgent

# Login to HuggingFace Hub
login(os.getenv("HUGGINGFACE_TOKEN"))

# Starcoder
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")

