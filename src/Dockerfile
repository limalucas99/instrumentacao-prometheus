FROM python:3.11.0
EXPOSE 5000
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
CMD ["sh", "/app/entrypoint.sh"]
