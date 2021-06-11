FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN python3 -m venv venv
RUN venv/bin/python3 -m pip install -r requirements.txt
CMD ["venv/bin/python3", "-m", "P0"]
