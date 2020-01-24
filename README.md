vutwifi
=====

Connect to WiFi at FIT VUT in Brno.

Install the package (requires Python 3.5 or newer):

	pip install vutwifi

Use on of the commands:

- `connect`     - Connect to VUT Wifi
- `disconnect`  - Disconnect from VUT Wifi
- `status`      - Check whether you are connected to the VUT WiFi
- `watch`       - Check for connection periodically and reconnect if needed

When connecting for the first time you will be prompted for username and
password which will be then written to `~/.vutwifi.conf`.
