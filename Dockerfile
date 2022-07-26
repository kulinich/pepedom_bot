FROM python:latest

WORKDIR /usr/app/src

COPY pepedom_bot.py .
COPY data_info.py .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install pytelegrambotapi

ENTRYPOINT [ "python", "pepedom_bot.py" ]