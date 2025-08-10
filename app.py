from flask import Flask, render_template, request, jsonify
import os
from utils.check_submission import check_submission
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


# Load Hugging Face model and tokenizer once at startup
MODEL_NAME = "distilgpt2"  # Very small, fast, and lightweight model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# List of labs
@app.route('/labs')
def labs():
    labs = [
        'Lab 1: Introduction to Python',
        'Lab 2: Data Structures',
        'Lab 3: Working with Lists',
        'Lab 4: String Manipulation',
        'Lab 5: Dictionary Operations'
    ]
    return render_template('labs.html', labs=labs)


# Lab details and instructions
@app.route('/lab/<lab_name>')
def lab_detail(lab_name):
    # Map lab titles to their markdown files
    lab_files = {
        'Lab 1: Introduction to Python': 'labs/lab1.md',
        'Lab 2: Data Structures': 'labs/lab2.md',
        'Lab 3: Working with Lists': 'labs/lab3.md',
        'Lab 4: String Manipulation': 'labs/lab4.md',
        'Lab 5: Dictionary Operations': 'labs/lab5.md',
    }
    filename = lab_files.get(lab_name)
    instructions = None
    if filename and os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            instructions = file.read()
    else:
        # fallback to auto-generated filename
        base = lab_name.lower().replace(" ", "_")
        fname = f'labs/{base}.md'
        if os.path.exists(fname):
            with open(fname, 'r', encoding='utf-8') as file:
                instructions = file.read()
        else:
            instructions = "Lab instructions not found."
    return render_template('lab_detail.html', lab_name=lab_name, instructions=instructions)

# Handle lab submissions
@app.route('/submit/<lab_name>', methods=['POST'])
def submit_lab(lab_name):
    user_submission = request.form['submission']
    feedback = check_submission(lab_name, user_submission)
    # If AJAX, return JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'feedback': feedback})
    # Fallback to old behavior
    return render_template('feedback.html', feedback=feedback)

@app.route('/ai-assist', methods=['POST'])
def ai_assist():
    user_question = request.json.get('question')
    lab_name = request.json.get('lab_name')
    # Improved prompt for better context and deterministic output
    prompt = (
        f"Lab: {lab_name}\nQuestion: {user_question}\nAnswer:"
    )
    try:
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
        with torch.no_grad():
            output_ids = model.generate(
                input_ids,
                max_new_tokens=40,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id if hasattr(tokenizer, 'eos_token_id') else None
            )
        answer = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        # Only return the part after 'Answer:'
        if 'Answer:' in answer:
            answer = answer.split('Answer:')[-1].strip()
        if not answer:
            answer = "Sorry, I couldn't generate an answer."
    except Exception as e:
        answer = f"Sorry, I couldn't get an answer from the AI. ({e})"
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)