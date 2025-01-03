FROM mcr.microsoft.com/devcontainers/python:3.12

WORKDIR /app
ADD app/app.py ./app.py
ADD app/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]