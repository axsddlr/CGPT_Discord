FROM python:3.9.5-slim-buster AS build

RUN mkdir -p /cgpt_bot

WORKDIR /cgpt_bot

RUN apt-get update && \
    apt-get install -y --no-install-recommends git gcc build-essential python-dev apt-utils -y

COPY requirements.txt .
RUN pip install --no-cache-dir  -r requirements.txt

FROM python:3.9.5-slim-buster AS final
WORKDIR /cgpt_bot
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . .

RUN chmod -R 777 .

CMD ["python", "bot.py"]
