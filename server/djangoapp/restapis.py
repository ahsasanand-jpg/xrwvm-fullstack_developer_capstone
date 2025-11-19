# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"
    request_url = f"{backend_url}{endpoint}"
    if params:
        request_url += "?" + params.rstrip("&")
    
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except Exception as e:
        print("Network exception occurred:", str(e))
        return {}


def analyze_review_sentiments(text):
    if not text or not text.strip():
        return {"sentiment": "none"}
    
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url, timeout=10)
        result = response.json()
        # Code Engine microservice returns {"sentiment": "positive"/"negative"/"neutral"}
        return result
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Sentiment analyzer microservice not reachable")
        return {"sentiment": "none"}


def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        print("Post review response:", response.json())
        return response.json()
    except Exception as e:
        print("Network exception occurred in post_review:", str(e))
        return {"status": 500, "message": "Error posting review"}