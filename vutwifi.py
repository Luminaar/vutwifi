import json
import time
from pathlib import Path

import click
import requests

URL = "https://wifigw.cis.vutbr.cz/login.php"
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
}
CONFIG_FILE_PATH = Path.home() / ".vutwifi.conf"


def check_user(user=None, password=None):
    """Check if 'user' in 'password' are set. If not, get them from user
    input."""

    if CONFIG_FILE_PATH.exists():
        content = CONFIG_FILE_PATH.read_text()
        try:
            config = json.loads(content)
            user = config.get("user")
            password = config.get("password")
        except json.decoder.JSONDecodeError:
            pass

    if not user or not password:

        if not user:
            user = input("Username: ")
        if not password:
            password = input("Password: ")

        CONFIG_FILE_PATH.write_text(json.dumps({"user": user, "password": password}))

    return user, password


@click.group()
def cli():
    pass


def is_connected():
    """Check whether you are connected to the internet.

    Return True if connected, False otherwise."""

    resp = requests.get(URL, headers=HEADERS)
    return 'input type="password"' not in resp.text


@cli.command(help="Check whether you are connected to the VUT WiFi")
def status():
    """Check whether you are connected to the internet.

    Return True if connected, False otherwise."""

    if is_connected():
        print("You are connected")
    else:
        print("You are disconnected")


def _connect(user, password):

    requests.post(
        URL, headers=HEADERS, data="user=%s&auth=any&password=%s" % (user, password)
    )


@cli.command(help="Connect to VUT Wifi")
def connect():
    user, password = check_user()

    _connect(user, password)


@cli.command(help="Disconnect from VUT Wifi")
def disconnect():
    requests.post(URL, headers=HEADERS, data="logout=1")


@cli.command(help="Check for connection periodically and reconnect if needed")
def watch(user=None, password=None, interval: int = 30):
    """Poll the internet connection periodically and reconnect if the
    connection is down.
    """

    user, password = check_user(user, password)

    while True:
        try:
            if not is_connected():
                print("Reconnecting")
                _connect(user, password)
            else:
                print("Connected")

            time.sleep(interval)
        except KeyboardInterrupt:
            break
