import requests
from app.schemas import QuestionAPI
from fastapi import HTTPException
from typing import List


def fetch_questions(num: int) -> List[QuestionAPI]:
    url = f"https://jservice.io/api/random?count={num}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [QuestionAPI(**question) for question in data]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch question from the public API: {str(e)}")
    