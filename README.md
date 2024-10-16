# Будьте очень осторожны, скрипт полностью рабочий но телеграм очень оперативно блокирует за его использование аккаунты


1. скачайте Python версии 3.12.7+
2. скачайте исходный код 
```sh
git clone https://github.com/gigorgu/telegram-avatar-time.git
```
3. в файле .ENV измените api на api вашей программы созданной на [my.telegram.org](https://my.telegram.org)
4. для тех кто не хочет работать в виртуальном окружении python просто напишите в консоль в любом месте 
```sh
pip install pillow python-dotenv aiofiles telethon
```
### рекомендации
1. создайте виртуальное окружение python
```sh
python3 -m venv .venv
```

2. активируйте его (важно чтобы в вашей ос - был powers shell 3+ который может выполнять скрипты самописные)
```sh
./.venv/scripts/activate # в случае ошибки тут, вы можете погуглить как дать права для powershell на выполнение custom сценариев
```

3. если вы все сделали правильно то у вас перед текстом в какой директории вы выполняете этот терминал должно быть написанно `(.venv)`, следовательно вы пишете и ждете выполнения установки
```sh
pip install pillow python-dotenv aiofiles telethon
```
.env preset
про файл env забыл написать крч его создаете и все там напишите вот что снизу написано можете под себя настраивать как угодно

```cs
API_ID=123456
API_HASH="1ab2cd3ef4g5"
SESSION_NAME=NULL
DEVICE_MODEL=NULL
SYSTEM_VERSION=NULL
SYSTEM_LANGUAGE=NULL
LANGUAGE_CODE=NULL
APP_VERSION=NULL
GMT=+3
```
