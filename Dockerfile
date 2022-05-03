FROM python:3.10
EXPOSE 80
RUN pip install fastapi uvicorn[standard]
COPY main.py .
CMD uvicorn --host 0.0.0.0 --port 80 main:app
