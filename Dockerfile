FROM python:3.10-slim

WORKDIR /Asambly
COPY Asambly/ /Asambly/

RUN pip install --no-cache-dir -r /Asambly/requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
