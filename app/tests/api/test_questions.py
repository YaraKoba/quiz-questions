from fastapi.testclient import TestClient


def test_add_new(client: TestClient) -> None:
    r = client.post(f"http://localhost:8000/questions/add-new", json={'questions_num': 10})
    questions = r.json()
    assert questions
    assert len(questions) == 10

