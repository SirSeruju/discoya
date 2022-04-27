# discoya

## Description
Discord bot for playing Yandex.Music playlists and tracks

## Run

### With kubernetes + helm
Create values.yaml and fill it with values:

    bot_id: ""
    bot_name: ""
    bot_prefix: ""
    bot_token: ""
    yandex_login: ""
    yandex_password: ""

then

    helm repo add discoya https://sirseruju.github.io/discoya/helm/repo
    helm install -n discoya --create-namespace -f values.yaml bot discoya/bot

### With docker-compose
Edit .env or docker-compose.yml or src/config.py, then

    docker-compose up -d
