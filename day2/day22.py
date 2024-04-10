
from transformers import pipeline
# from pathlib import Path


pipe = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
# mypath = str(Path.cwd())
response = pipe("https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg")

print(response)