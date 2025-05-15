""" This script is used to load a pre-trained GPT-2 model and tokenizer from a local directory 
and generate text based on a user-provided prompt."""

# Import necessary libraries
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load tokenizer and model from local directory where they are saved from notebook
tokenizer = AutoTokenizer.from_pretrained("notebook/model/gpt2-medium")
model = AutoModelForCausalLM.from_pretrained("notebook/model/gpt2-medium")

# Set up the text generation pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    pad_token_id=tokenizer.eos_token_id,
    temperature=0.9
)

# Generate text from a given prompt
def generate_text(prompt, max_length=150):
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return result[0]['generated_text']
