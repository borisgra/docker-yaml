FROM python:3.12-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY --chmod=777 . /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["cloudrun.py"]
