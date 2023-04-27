FROM python:3.8-alpine
WORKDIR /usr/src/api
ADD requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--port", "8000"]