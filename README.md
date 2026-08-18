# Мини-анкета — Full-stack приложение

Простое full-stack приложение «Мини-анкета» на **Python (FastAPI)** + **HTML/JS**.

## Функционал

- **Backend** (FastAPI):
  - `GET /questions` — возвращает список вопросов анкеты (5 вопросов)
  - `POST /answers` — принимает ответы пользователя и сохраняет их в памяти
  - `GET /answers` — возвращает все сохранённые ответы (для отладки)
  - `GET /` — отдаёт HTML-страницу анкеты

- **Frontend** (чистый HTML + JS):
  - Загружает вопросы с backend через `GET /questions`
  - Отображает форму с валидацией обязательных полей
  - Отправляет ответы через `POST /answers`
  - Показывает сообщение «Спасибо!» после успешной отправки

## Структура проекта

```
test1/
├── main.py              # Backend: FastAPI приложение
├── requirements.txt     # Python зависимости
├── run_tests.py         # Тесты API (TestClient)
├── static/
│   └── index.html       # Frontend: HTML/JS интерфейс
└── README.md            # Документация
```

## Запуск

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск сервера

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### 3. Открытие приложения

Откройте в браузере: **http://127.0.0.1:8000**

### 4. Проверка API

```bash
# Получить вопросы
curl http://127.0.0.1:8000/questions

# Отправить ответы
curl -X POST http://127.0.0.1:8000/answers \
  -H "Content-Type: application/json" \
  -d '{"answers": [{"question_id": 1, "value": "Иван"}, {"question_id": 2, "value": "25"}]}'

# Посмотреть сохранённые ответы
curl http://127.0.0.1:8000/answers
```

### 5. Запуск тестов

```bash
pip install httpx
python run_tests.py
```

## Технологии

| Компонент | Технология |
|-----------|------------|
| Backend   | Python 3.13, FastAPI, Uvicorn |
| Frontend  | HTML5, CSS3, Vanilla JavaScript |
| API       | REST (GET/POST), JSON |

## Вопросы анкеты

1. Как вас зовут? *(обязательно)*
2. Сколько вам лет? *(обязательно)*
3. Какой ваш любимый язык программирования? *(обязательно)*
4. Оцените курс от 1 до 10 *(обязательно)*
5. Ваши пожелания и комментарии *(необязательно)*