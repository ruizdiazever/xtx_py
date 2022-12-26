def set_output(title: str, body: str, extradata: str):
    """ Return a dictionary with colored and plain text """
    title_color = colored(title, "yellow")
    return {
        "colored": f"{title_color}: {body}\nHTML: {extradata}\n",
        "plain": f"{title}: {body}\nHTML: {extradata}\n"
    }


def api_telegram(token: str, chat_id: str, message: str) -> str:
    """ Return url to request with API Telegram """
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    return url


def colored(text: str, color: str):
    """ Return string in color with ANSI codes """

    if color == "red":
        text = f"\033[91m{text}\033[00m"
    elif color == "yellow":
        text = f"\033[93m{text}\033[00m"
    elif color == "green":
        text = f"\033[92m{text}\033[00m"
    elif color == "cyan":
        text = f"\033[96m{text}\033[00m"
    elif color == "gray":
        text = f"\033[90m{text}\033[00m"
    else:
        pass
    return text
