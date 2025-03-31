Použitý NLP stack:
Technológia	Úloha
Python + spaCy / NLTK / Transformers (Hugging Face)	Spracovanie textu, tokenizácia, entitná analýza
Text classification (fine-tuned BERT alebo SVM)	Rozpoznávanie typu požiadavky
Sentiment analysis (napr. vaderSentiment, BERT)	Emocionálny tón správy
Named Entity Recognition (NER)	Rozpoznanie údajov ako číslo faktúry, meno, e-mail
FastAPI alebo Flask	Backend API pre spracovanie správ
Redis	Cache výsledkov pre opakované požiadavky
PostgreSQL / SQLite	Ukladanie správ a výsledkov analýzy

Funkcie aplikácie:
- Analyzuje npríklad e-mailový text alebo správu zo support formulára
- Určí, či ide o: Reklamáciu/Kritickú sťažnosť/Dotaz na faktúru/Všeobecnú otázku
- Vyhodnotí emóciu: pozitívna / neutrálna / negatívna
- Rozpozná mená, dátumy, čísla faktúr
- Priradí správu do správneho frontu support tímu

setup_env.bat>>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn main:app --reload
