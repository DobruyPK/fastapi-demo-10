FROM python:3.8-alpine
WORKDIR /usr/src/api
ADD requirements.txt .
ADD main.py .


RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]