
# Career Orientation FAQ Chatbot

This is a FAQ Chatbot built as part of my internship at **CodeAlpha**.

The chatbot answers common questions related to career guidance, resume building, interviews, skills, and internships.

## Features
- Answers career-related FAQs
- Uses TF-IDF and Cosine Similarity for matching questions
- Text preprocessing
- Two ways to run the chatbot (Terminal + Web Interface)

## Technologies Used
- Python
- scikit-learn
- NumPy
- Streamlit

## How to Run

### Method 1: Terminal Version
1. Install the required libraries:
```bash
pip install -r requirements.txt

2. Run the chatbot:
```bash
python chatbot.py
3. Type your question and press Enter.
4. Type `exit` to quit.

### Method 2: Web Interface (Streamlit)
1. Install the required libraries:
```bash
pip install -r requirements.txt

2. Run this command:

python app.py
3. A link will appear in the terminal (example: http://localhost:8501)
4. Press `Ctrl` and click on the link to open the chatbot in your browser.

## Project Structure
- `chatbot.py` → Terminal version of the chatbot
- `app.py` → Streamlit web version of the chatbot
- `faq_data.py` → Contains all FAQ questions and answers
- `requirements.txt` → List of required libraries

## Author Name
Joycee Khude.
CodeAlpha Intern.
