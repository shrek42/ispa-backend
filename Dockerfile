FROM python:3-alpine

WORKDIR /app/backend
VOLUME /app/backend

ADD app/ ./app
COPY setup.py run.py ./

RUN pip install -e .

EXPOSE 5000

#ENTRYPOINT ["python3", "run.py"]
