import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faq_data import faqs

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join(text.split())
    return text

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)

def get_answer(user_question):
    processed_user_q = preprocess(user_question)

    user_tfidf = vectorizer.transform([processed_user_q])

    similarities = cosine_similarity(user_tfidf, tfidf_matrix)

    best_match_index = np.argmax(similarities)

    best_score = similarities[0][best_match_index]

    if best_score < 0.45:
        return "Sorry, I couldn't understand your question. Please ask something related to career orientation."

    return answers[best_match_index]