from transformers import pipeline

generator = pipeline('text-generation', model="facebook/opt-350m", device=0)
generator("What are we having for dinner?")

# NotImplementedError