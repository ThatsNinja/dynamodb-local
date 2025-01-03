FROM mcr.microsoft.com/devcontainers/python:3.12

WORKDIR /app
ADD app.py ./app.py
ADD requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run"]