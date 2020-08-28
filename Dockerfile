FROM python:3

WORKDIR /bot

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["utilitybot.py"]