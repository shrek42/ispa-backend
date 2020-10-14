FROM python:3-alpine

WORKDIR /

ADD app/ ./app
COPY setup.py run.py ./

RUN pip install -e .

EXPOSE 5000

ENTRYPOINT ["python", "run.py"]
