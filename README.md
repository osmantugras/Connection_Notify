## This script is made for macOS.

These python scripts detect connections for some hosts.
It sends notifications according to the status of the connection.
You can also edit the Host address.
In these scripts used google addresse to test the script.
Notifications were made according to macOS.

# Network Connection Notifier

This script sends notifications to the user when the network connection status changes. It uses the macOS `Foundation` and `AppKit` frameworks to display notifications. When the network connection is established or lost, a notification is sent to inform the user.

## Dependencies

- Python 3.x
- `colorama` library (install using `pip install colorama`)

## How to Run

1. Make sure you have Python 3.x installed on your macOS system.

2. Install the `colorama` library by running the following command:

3. Clone this repository or download the script file.

4. Open a terminal and navigate to the directory where the script file is located.

5. Run the following command to execute the script:

6. The script will continuously check the network connection status by pinging a specified hostname (default is "google.com"). When the network connection is established, a notification with the title "Network Connection", subtitle "Network Connection", and informative text "Network Connection is UP" will be displayed. When the network connection is lost, a notification with the same title and subtitle but with the informative text "Network Connection is Down" will be displayed.

7. Additionally, the script will write a message to the console indicating the notification has been sent.

8. The script will wait for the network connection to be reestablished and repeat the process.

9. To stop the script, press `Ctrl + C` in the terminal.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any damages or liabilities caused by the use of this script.
