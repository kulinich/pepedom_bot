# pepedom_bot
Бот для тг-группы Собственники ЖК "Полюстрово парк"

Как использовать:

1. Создаем бота у BotFather'а
2. Создаем docker образ:
    docker image build -t pepedom_bot:0.0.1 .
3. Запускаем через Docker:
    docker run --rm -d pepedom_bot:0.0.1 -t BOT_TOKEN -c CHAT_ID
