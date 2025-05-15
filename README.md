
# 🧠 GPT Text Generator Tool

A web-based application that generates human-like text using the **GPT-2 Medium** model. This project uses Hugging Face Transformers and Flask to provide an interactive interface for text generation.

---

## 🚀 Features

- Text generation using the `GPT-2 Medium` model
- Web interface built with Flask
- Simple prompt-based input
- Download model using provided Jupyter Notebook
- Lightweight and easy to run locally



## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```


## 🧰 How to Use

1. **Clone the repository**

```bash
git clone https://github.com/sairao4102/GPT-TEXT-GENERATOR-TOOL.git
cd GPT-TEXT-GENERATOR-TOOL
```

2. **Download the GPT-2 Medium model**

Since the model file (1.3+ GB) is too large to be uploaded to GitHub, you need to download it  running the notebook file
Model files are **not included** in the repo. Run this in the notebook to download them:

> 🧾 Run the Jupyter Notebook provided:

```bash
notebook/Untitled5.ipynb
```

This will automatically download the `gpt2-medium` model and tokenizer from Hugging Face.

3. **Run the application**

```bash
python app.py
```

This project was developed as part of my internship at ** CODTECH IT Solutions** (Task 4).


