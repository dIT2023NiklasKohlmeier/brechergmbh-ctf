FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN echo "FLAG{Traversal_Master_Level_1}" > /app/flag.txt

EXPOSE 5000

CMD ["python", "app.py"]