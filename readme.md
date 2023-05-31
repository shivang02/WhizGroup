<!-- center the title and add a line below the title -->
<h1 align="center">WhizGroup: A WhatsApp Group Maker</h1>

<!-- These are the badges for the project. You can add more badges by copying the code below and changing the links to the appropriate ones for your project from https://shields.io/ -->
<p align="center">
  <img src="https://img.shields.io/github/license/shivang02/whizgroup?style=flat-square" alt="License" />
  <img src="https://img.shields.io/github/languages/code-size/shivang02/whizgroup?style=flat-square" alt="Code Size" />
  <img src="https://img.shields.io/github/last-commit/shivang02/whizgroup?style=flat-square" alt="Last Commit" />
  <img src="https://img.shields.io/github/issues/shivang02/whizgroup?style=flat-square" alt="Issues" />
  <img src="https://img.shields.io/github/forks/shivang02/whizgroup?style=flat-square" alt="Forks" />
  <img src="https://img.shields.io/github/stars/shivang02/whizgroup?style=flat-square" alt="Stars" />
</p>

This program automates the process of creating WhatsApp groups by adding contacts from a CSV file to a new group. It utilizes the Selenium library to control the Chrome web browser and perform the necessary operations on WhatsApp Web.

## Setting up a virtual environment (Optional):

1. Open your terminal or command prompt and navigate to the directory where you want to create the virtual environment. You can use the `cd` command to change the directory.

3. Run the following command to create a virtual environment:

   For Windows:
   ```bash
   python -m venv myenv
   ```

   For Unix/Linux/Mac:
   ```bash
   python3 -m venv myenv
   ```

   This command creates a virtual environment named "myenv" in the current directory.

4. Activate the virtual environment:

   For Windows:
   ```bash
   myenv\Scripts\activate
   ```

   For Unix/Linux/Mac:
   ```bash
   source myenv/bin/activate
   ```

   After running this command, you will see the virtual environment name (e.g., "myenv") in your command prompt, indicating that the virtual environment is active.

Now, you have successfully created and activated the virtual environment. You can proceed with installing packages and running your project within the virtual environment.

## Installation

1. Clone the repository or download the code.
2. Install the required dependencies by running the following command:

   ```bash
   pip install selenium pandas ttkthemes webdriver_manager
   ```

    This will install the necessary Python packages to run the program.

    Note: If you are using a virtual environment, make sure to activate it before running the above command.
<!-- optional installation instructions for setting up a virtual environment -->

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

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

Please make sure to install the required dependencies before running the code. You can follow the installation instructions provided in the readme.