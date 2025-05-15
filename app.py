""" This is a simple Flask web application that allows users to input a prompt 
 and receive generated text in response."""

# Import necessary libraries
from flask import Flask, render_template, request
from generate import generate_text  # Import the function to generate text using a model (e.g., GPT)

# Initialize the Flask application
app = Flask(__name__)

# Define the main route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""  
    if request.method == "POST":
        # Get user input from the form
        prompt = request.form.get("prompt")
        if prompt:
            output = generate_text(prompt)
    return render_template("index.html", output=output)

# Run the app in debug mode (useful during development)
if __name__ == "__main__":
    app.run(debug=True)
