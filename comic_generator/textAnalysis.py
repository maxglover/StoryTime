import spacy
from transformers import pipeline

nlp = spacy.load('en_core_web_sm')
sentiment_analysis = pipeline('sentiment-analysis')

def analyze_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentiment = sentiment_analysis(text)
    return entities, sentiment
