import spacy
from transformers import pipeline

nlp = spacy.load('en_core_web_sm')
sentiment_analysis = pipeline('sentiment-analysis')

def analyze_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentiment = sentiment_analysis(text)
    dialogue = extract_dialogue(text)
    return entities, sentiment, dialogue

def extract_dialogue(text):
    # A simple approach to find dialogue enclosed in quotation marks
    import re
    dialogue = re.findall(r'“([^”]*)”|\"([^\"]*)\"', text)
    # Flatten the list and remove empty strings
    dialogue = [line for group in dialogue for line in group if line]
    return dialogue
