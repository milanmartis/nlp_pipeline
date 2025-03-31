import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

# Jednoduchá kategorizácia podľa kľúčových slov
CATEGORIES = {
    "invoice": ["invoice", "billing", "payment"],
    "complaint": ["complaint", "problem", "issue", "not working"],
    "general": ["question", "info", "information", "help"]
}

def classify(text):
    text_lower = text.lower()
    for category, keywords in CATEGORIES.items():
        if any(word in text_lower for word in keywords):
            return category
    return "uncategorized"

def analyze_text(text):
    doc = nlp(text)

    # Extrahovanie entít
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    # Sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # Kategória
    category = classify(text)

    return {
        "category": category,
        "sentiment": sentiment,
        "entities": entities
    }