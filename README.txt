This is the user documentation for FLAIR. This document provides guidance on how to
run the source code to be able to use FLAIR’s functionality effectively.

A. Getting Started
A.1 System Requirements
Before using FLAIR, ensure that your system meets the following requirements:
1. Your desktop PC or laptop has Windows, macOS, or Linux (Ubuntu/Debian) as its
operating system.
2. Your device has the latest version of Python and Java installed. If not, please
check https://python.org/downloads/ to download Python and java.com/en/download/manual.jsp
to download the appropriate Java Development Kit (JDK) installer suitable for
your operating system.

A.2 Accessing FLAIR
Access FLAIR through the following steps:
1. Go to FLAIR’s Github repository (https://github.com/aliaolay/FLAIR) 
and copy its HTTPS or SSH URL. You can find this URL on the repository’s main page.
2. Navigate to your desired directory where you want to clone the repository using the following command 
on Command Prompt (on Windows) or Terminal (macOS/Linux): cd /path/to/directory.
3. Use the ‘git clone‘ command followed by the repository URL (HTTPS/SSH) to clone
the repository to your device: git clone (https/ssh url).
4. To verify that cloning has been successful, you should see a new directory with the
repository name inside your specified directory.

A.3 Repository Overview and Use
FLAIR’s repository contains the following folders and files:
1. File: REQUIREMENTS.txt
• This text file is a compilation of all needed libraries and packages FLAIR
requires.
• To proceed with installation, launch Command Prompt (for Windows) or Terminal 
(for macOS and Linux (Debian/Ubuntu)) and go to FLAIR’s repository
directory on your device.
• Then, enter the following command: pip install -r requirements.txt and press
Enter. Wait for all installations to complete.

2. Folder: flair
• This folder contains the Django project to be ran in order to access the web
application for end users.
• To run the application, ensure that your current directory is set to this folder then 
enter the following command: python manage.py runserver
• After successfully starting the application, you may access it through 'http://localhost/'
or 'http://127.0.0.1/' on your web browser.

3. file: README.txt
• This file lists the steps and requirements neeeded to run the FLAIR application.