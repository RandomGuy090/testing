FROM python:latest
WORKDIR /app
CMD pip3 install -r requirements.txt
COPY . .

ENV VERSION="0.1"
ENV PORT="5009"

EXPOSE 5009/tcp

CMD ["python3",  "run.py"]