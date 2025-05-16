
#  GPT Text Generator Tool

A web-based application that generates human-like text using the **GPT-2 Medium** model. This project uses Hugging Face Transformers and Flask to provide an interactive interface for text generation.

---

##  Features

- Text generation using the `GPT-2 Medium` model
- Web interface built with Flask
- Simple prompt-based input
- Download model using provided Jupyter Notebook
- Lightweight and easy to run locally

  
## Technologies Used
- **Transformers (Hugging Face)**: For using the pre-trained GPT-2 Medium model to generate text based on user input.

- **Flask**: Backend framework to handle user requests and serve model-generated responses.

- **HTML/CSS**: To design a clean, responsive web interface.

- **JavaScript**: For enhancing user interactions on the frontend.

- **Jupyter Notebook**: Used for running and testing model behavior interactively.

## How It Works
- **User Input**:
Users enter a prompt into the web interface.

- **Text Generation**:
The backend loads the GPT-2 Medium model and generates a continuation of the prompt using Hugging Face's transformers library.

- **Display Output**:
The generated text is returned to the user on the webpage.

- **Model Setup**:
The model files are not included in the GitHub repo due to size constraints. Instead, users are guided to download the model by running the provided Jupyter notebook (Untitled5.ipynb), which will fetch and cache the necessary files automatically.



##  How to Use

### 1. **Clone the repository**

```bash
git clone https://github.com/sairao4102/GPT-TEXT-GENERATOR-TOOL.git
cd GPT-TEXT-GENERATOR-TOOL
```

### 2.  Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

### 3. **Download the GPT-2 Medium model**

Since the model file (1.3+ GB) is too large to be uploaded to GitHub, 
Model files are **not included** in the repo. Run this in the notebook to download them:

> 🧾 Run the Jupyter Notebook provided:

```bash
notebook/Untitled5.ipynb
```

This will automatically download the `gpt2-medium` model and tokenizer from Hugging Face.

### 4. **Run the application**

```bash
python app.py
```

Access the Application:
Web Interface: Open [http://127.0.0.1:5000] in your browser


This project was developed as part of my internship at ** CODTECH IT Solutions** (Task 4).


