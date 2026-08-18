import subprocess
import time
import urllib.request
import json
import sys

# Запуск сервера
proc = subprocess.Popen(
    [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"],
    cwd="C:/Users/rpavlov/otus/test1",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

time.sleep(4)

results = []

try:
    # Тест GET /questions
    resp = urllib.request.urlopen("http://127.0.0.1:8001/questions")
    questions_data = json.loads(resp.read().decode())
    results.append("=== GET /questions ===")
    results.append(json.dumps(questions_data, ensure_ascii=False, indent=2))
    results.append("")

    # Тест POST /answers
    payload = json.dumps({
        "answers": [
            {"question_id": 1, "value": "Иван"},
            {"question_id": 2, "value": "25"},
            {"question_id": 3, "value": "Python"},
            {"question_id": 4, "value": "9"},
            {"question_id": 5, "value": "Отличный курс!"},
        ]
    }).encode("utf-8")

    req = urllib.request.Request(
        "http://127.0.0.1:8001/answers",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    resp = urllib.request.urlopen(req)
    answers_data = json.loads(resp.read().decode())
    results.append("=== POST /answers ===")
    results.append(json.dumps(answers_data, ensure_ascii=False, indent=2))
    results.append("")

    # Тест GET /answers (проверка сохранения)
    resp = urllib.request.urlopen("http://127.0.0.1:8001/answers")
    stored_data = json.loads(resp.read().decode())
    results.append("=== GET /answers (сохранённые) ===")
    results.append(json.dumps(stored_data, ensure_ascii=False, indent=2))
    results.append("")

    results.append("ALL TESTS PASSED!")

except Exception as e:
    results.append(f"ERROR: {e}")
finally:
    proc.terminate()
    proc.wait()

# Запись результатов
with open("C:/Users/rpavlov/otus/test1/test_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("Tests completed. Results written to test_results.txt")