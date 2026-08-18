from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
import uuid

app = FastAPI(title="Мини-анкета", version="1.0.0")

# Хранилище ответов в памяти
answers_store: list[dict] = []

# Жёстко заданные вопросы анкеты
QUESTIONS = [
    {
        "id": 1,
        "text": "Как вас зовут?",
        "type": "text",
        "required": True,
    },
    {
        "id": 2,
        "text": "Сколько вам лет?",
        "type": "number",
        "required": True,
    },
    {
        "id": 3,
        "text": "Какой ваш любимый язык программирования?",
        "type": "text",
        "required": True,
    },
    {
        "id": 4,
        "text": "Оцените курс от 1 до 10",
        "type": "number",
        "required": True,
    },
    {
        "id": 5,
        "text": "Ваши пожелания и комментарии",
        "type": "text",
        "required": False,
    },
]


# Модель для приёма ответов
class AnswerItem(BaseModel):
    question_id: int
    value: str


class AnswersPayload(BaseModel):
    answers: list[AnswerItem]


@app.get("/questions")
def get_questions():
    """Возвращает список вопросов анкеты."""
    return {"questions": QUESTIONS}


@app.post("/answers")
def submit_answers(payload: AnswersPayload):
    """Принимает ответы пользователя и сохраняет их в памяти."""
    record = {
        "id": str(uuid.uuid4()),
        "answers": [a.model_dump() for a in payload.answers],
    }
    answers_store.append(record)
    return {"status": "ok", "message": "Спасибо!", "id": record["id"]}


@app.get("/answers")
def get_answers():
    """Возвращает все сохранённые ответы (для отладки)."""
    return {"answers": answers_store, "total": len(answers_store)}


# Раздача фронтенда
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.get("/", response_class=HTMLResponse)
def index():
    """Отдаёт HTML-страницу анкеты."""
    index_path = static_dir / "index.html"
    return index_path.read_text(encoding="utf-8")