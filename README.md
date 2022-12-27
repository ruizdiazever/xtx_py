# Scapring Bot 🤖

I create this bot to get a GPU xD, work searching stock in differents sites (scraping the site) and send me a message in Telegram when the stock is available.

## Requirements 📝

* Your [Telegram bot](https://core.telegram.org/bots)
* Python >= 3.11

## Want to try it? 😁

1. Create a `.env` file with your Telegram credentials.

    ```bash
    TELEGRAM_TOKEN=''
    TELEGRAM_CHAT_ID=''
    ```

2. Set your links and user agents in `settings.py`, example:

    * **name:** name to identifier the site shop.
    * **url:** url of product in site shop.
    * **type:** class or id (HTML element) containing the availability message.
    * **typeKey:** key of id or class
    * **noStockString:** no available message in product shop site (the bot send you a message if this string dont exist)
    * **active:** you can add many links and deactivate some if you want.

    ```python
    LINKS = [
        {
            "name": "Armazon",
            "url": "https://www.armazon.it/lalalolo",
            "type": "id",
            "typeKey": "availability",
            "noStockString": "Non disponibile.",
            "active": True
        }
    ]
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
    ]
    ```

3. Run

    ```bash
    sh docker.sh
    ```

## Useful commands 🐧

```bash
ps aux | grep python               # See active process 
cd /proc/$pid/fd && tail -f *      # See proc with PID
du -sh logs.log                    # See size of file
docker logs -f $cointainerID       # See live logs
bashtop                            # See system monitor
docker exec -it $containerId bash  # Bash in container
```

## Info ℹ️

* [Installation of Docker in Raspberry OS](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script)
* [Telegram docs about bot messages](https://core.telegram.org/bots/api#message)
