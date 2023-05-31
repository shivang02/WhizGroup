# WhatsApp Group Maker

This program automates the process of creating WhatsApp groups by adding contacts from a CSV file to a new group. It utilizes the Selenium library to control the Chrome web browser and perform the necessary operations on WhatsApp Web.

## Installation

1. Clone the repository or download the code.
2. Install the required dependencies by running the following command:

   ```bash
   pip install selenium pandas ttkthemes webdriver_manager
   ```

   This will install the necessary Python packages to run the program.

## Usage

1. Make sure you have the Chrome web browser installed on your system.
2. Run the following command to start the WhatsApp Group Maker:

   ```bash
   python main.py
   ```

   This will open a graphical user interface (GUI) window.
3. In the GUI window, click the "Browse" button to select a CSV file containing the contacts you want to add to the WhatsApp group.
4. Click the "Start" button to begin the process.
5. Within 40 seconds, log in to WhatsApp Web using your credentials.
6. The program will automatically perform the following steps:
   - Download the Chrome driver if it is not already available on your system.
   - Open WhatsApp Web in a new Chrome browser window.
   - Add the contacts from the CSV file to a new group.
   - Click the "Next" button to proceed to the next step.
7. Wait for the group to be created, the group name to be entered, and the group to be opened.

Note: The program uses Selenium to control the web browser and perform the necessary operations. It may take some time to execute, depending on the number of contacts and the speed of your internet connection.

## Motivation

Creating WhatsApp groups manually can be time-consuming, especially when dealing with a large number of contacts. This project aims to simplify the process and save users' time by automating the group creation process.

Feel free to modify and enhance the code according to your requirements.

## License

This project is licensed under the MIT License. See the [LICENSE]()

---

Please make sure to install the required dependencies before running the code. You can follow the installation instructions provided in the readme.