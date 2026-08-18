from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

results = []

# Тест 1: GET /questions
resp = client.get("/questions")
assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
data = resp.json()
assert "questions" in data
assert len(data["questions"]) == 5
results.append("✓ GET /questions — 200 OK, 5 вопросов")
results.append(json.dumps(data, ensure_ascii=False, indent=2))

# Тест 2: POST /answers
payload = {
    "answers": [
        {"question_id": 1, "value": "Иван"},
        {"question_id": 2, "value": "25"},
        {"question_id": 3, "value": "Python"},
        {"question_id": 4, "value": "9"},
        {"question_id": 5, "value": "Отличный курс!"},
    ]
}
resp = client.post("/answers", json=payload)
assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
data = resp.json()
assert data["status"] == "ok"
assert data["message"] == "Спасибо!"
results.append("✓ POST /answers — 200 OK, статус 'ok', сообщение 'Спасибо!'")
results.append(json.dumps(data, ensure_ascii=False, indent=2))

# Тест 3: GET /answers (проверка сохранения)
resp = client.get("/answers")
assert resp.status_code == 200
data = resp.json()
assert data["total"] == 1
assert len(data["answers"]) == 1
results.append("✓ GET /answers — ответ сохранён в памяти")
results.append(json.dumps(data, ensure_ascii=False, indent=2))

# Тест 4: GET / (фронтенд)
resp = client.get("/")
assert resp.status_code == 200
assert "Мини-анкета" in resp.text
results.append("✓ GET / — HTML страница загружается")

print("\n".join(results))
print("\n=== ВСЕ ТЕСТЫ ПРОЙДЕНЫ! ===")