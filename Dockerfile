FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . code/

CMD ["fastapi", "run", "src/server.py", "port", "80"]