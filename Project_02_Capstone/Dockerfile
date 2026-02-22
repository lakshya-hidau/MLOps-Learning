FROM python:3.10-slim as base

WORKDIR /app

COPY flask_app/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY flask_app/ /app/

COPY models/vectorizer.pkl /app/models/vectorizer.pkl

RUN python -m nltk.downloader stopwords wordnet

EXPOSE 5000

#local
# CMD ["python", "app.py"]  

#Prod
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]