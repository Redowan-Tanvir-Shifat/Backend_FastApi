# FastAPI Documentation

## Introduction
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to simplify the development of robust and high-performing APIs while providing developers with tools to ensure code readability and maintainability. FastAPI leverages Python's type system, offering automatic request validation, serialization, and interactive documentation out of the box.

---

## Why Use FastAPI Over Other Frameworks
FastAPI stands out among other frameworks like Flask and Django for several reasons:

1. **Performance**: FastAPI is one of the fastest Python web frameworks, thanks to its asynchronous capabilities and ASGI support.
2. **Type Safety**: It uses Python type hints, which help catch errors early during development.
3. **Automatic Documentation**: Built-in support for OpenAPI and JSON Schema automatically generates Swagger UI and ReDoc documentation.
4. **Ease of Use**: The framework is intuitive and designed for both beginners and experienced developers.
5. **Dependency Injection**: Built-in support for dependency injection improves code modularity and reusability.
6. **Validation and Serialization**: Automatic request validation and response serialization are powered by Pydantic.

### Comparison with Other Frameworks
| Feature            | FastAPI           | Flask         | Django        |
|--------------------|-------------------|---------------|---------------|
| Performance        | High (ASGI-based) | Medium        | Medium        |
| Type Safety        | Strong (type hints) | Weak          | Weak          |
| Automatic Docs     | Yes               | No            | No            |
| Async Support      | Yes               | Partial       | Partial       |
| Validation/Parsing | Built-in (Pydantic) | Manual        | Manual        |

---

## Pros and Cons of FastAPI

### Pros
- **High Performance**: Built on Starlette and Pydantic, offering excellent performance.
- **Interactive Documentation**: Automatic and interactive API documentation with Swagger UI and ReDoc.
- **Type Safety**: Ensures robust code with type hints and validation.
- **Ease of Learning**: Clear syntax and good documentation make it beginner-friendly.
- **Asynchronous**: Supports asynchronous programming, making it ideal for high-concurrency applications.
- **Dependency Injection**: Facilitates modular development.

### Cons
- **Learning Curve**: For developers unfamiliar with type hints or asynchronous programming, there may be a slight learning curve.
- **Community Size**: Compared to older frameworks like Flask and Django, the community is smaller (though rapidly growing).
- **Limited Plugins**: Fewer third-party extensions and plugins compared to more established frameworks.

---

## Installation

Install FastAPI and its ASGI server (Uvicorn) using pip:

```bash
pip install fastapi
pip install uvicorn[standard]
```

---

## Creating a Simple API

Here's a quick example to get started:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### Running the Application

Run the application using Uvicorn:

```bash
uvicorn main:app --reload
```

Navigate to `http://127.0.0.1:8000` to see the API in action.

### Interactive API Documentation

FastAPI automatically generates interactive documentation:

- OpenAPI docs: `http://127.0.0.1:8000/docs` (Swagger UI)
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Path Parameters

Define path parameters by including them in the endpoint's route:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Path parameters are automatically validated based on their type hints.

---

## Query Parameters

Query parameters are declared as function arguments with default values:

```python
@app.get("/search")
def search_items(query: str, limit: int = 10):
    return {"query": query, "limit": limit}
```

---

## Request Body

FastAPI uses Pydantic models to validate request bodies:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

---

## Response Models

You can define response models for your endpoints:

```python
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
```

FastAPI validates the response data based on the response model.

---

## Dependency Injection

FastAPI provides a powerful dependency injection system:

```python
from fastapi import Depends

def common_dependency():
    return {"key": "value"}

@app.get("/items/")
def read_items(dep: dict = Depends(common_dependency)):
    return dep
```

---

## Middleware

Add custom middleware for pre/post-processing requests:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Error Handling

Handle errors with custom exception handlers:

```python
from fastapi import HTTPException

@app.get("/error")
def raise_error():
    raise HTTPException(status_code=404, detail="Item not found")
```

---

## Background Tasks

Run background tasks using `BackgroundTasks`:

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as log:
        log.write(message + "\n")

@app.post("/tasks/")
def create_task(background_tasks: BackgroundTasks, message: str):
    background_tasks.add_task(write_log, message)
    return {"message": "Task added"}
```

---

## Testing

Test your FastAPI application using Python's `pytest` framework:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
```

---

## Conclusion

FastAPI is an excellent choice for building modern APIs quickly and efficiently. Its seamless integration with Python's type hints, automatic documentation generation, and built-in features make it a powerful framework for developers. While it has a slight learning curve for beginners unfamiliar with asynchronous programming, its benefits far outweigh its cons, making it a top choice for API development.
