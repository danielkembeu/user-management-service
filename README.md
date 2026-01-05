# User Management Service

This project is a RESTful API for managing users, built with **FastAPI** and **SQLModel** using an SQLite database.

## Features

- Create, read, update, and delete user records (CRUD)
- Structured response messages for API endpoints
- Database setup and migrations handled at startup
- Modular design with easy route extension

## Requirements

- Python 3.8+
- `fastapi`
- `sqlmodel`
- `uvicorn`

You can install the required dependencies with:

```bash
pip install "fastapi[standard]" sqlmodel
```

## Project Structure

```
src/
├── api/
│   └── v1/
│       └── routes/
│           └── user_routes.py    # User CRUD API endpoints
├── database/
│   └── setup.py                  # DB setup, engine, and session utilities
├── models/
│   └── user_model.py             # User SQLModel definition
├── server.py                     # FastAPI app instantiation, db lifecycle
```

## Running the Application

From the `src/` directory, start the development server with:

```bash
uvicorn server:server --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Interactive API docs:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Example Endpoints

- **GET** `/users` — List users
- **GET** `/users/user/{user_id}` — Get a single user by ID
- **POST** `/users/create` — Create a new user
- **PUT** `/users/update/{user_id}` — Update an existing user
- **DELETE** `/users/{user_id}` — Delete a user

## Notes

- The SQLite database (`users_management.db`) is created automatically in the project root upon startup.
- If you change models, delete the database file to allow the app to regenerate it.
- Default error and response messages are provided for common API scenarios.

## License

MIT
