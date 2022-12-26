# Scapring Bot 🤖

This bot is to get a GPU xD

## Requirements 📝

* Your [Telegram bot](https://core.telegram.org/bots)
* Python >= 3.11

## Want to try it? 😁

1. Create a `.env` file with your phone number and your Coinbase and Telegram credentials.

    ```bash
    TELEGRAM_TOKEN=''
    TELEGRAM_CHAT_ID=''
    ```

2. Set your links and settings in `links.py`, example:

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
