# Step-by-Step Installation Guide

## Step 1: Go to the Project Repository
- Navigate to: [https://github.com/stephanbludward/Movie-finder/](https://github.com/stephanbludward/Movie-finder/)

## Step 2: Download the ZIP File
- Click on the green **"Code"** button.
- Select **"Download ZIP"**.

## Step 3: Extract the ZIP File
- Locate the downloaded ZIP file (usually in your **Downloads** folder).
- Right-click on the ZIP file and choose **"Extract All..."** or **"Extract Here"** (depending on your operating system).
- Make sure to remember where you extracted the files so you can find them later.

## Step 4: Open Command Prompt or a Terminal
- **Windows**: Press `Windows + R`, type `cmd`, and press **Enter**.
- **macOS/Linux**: Open your terminal from the applications or press `Ctrl + Alt + T`.

## Step 5: Copy the Path to the Folder You Extracted
- Open the folder where you extracted the ZIP file.
- **Windows**: Click on the address bar and **copy the full path**.
- **macOS/Linux**: Right-click and choose **"Copy as Path"**.

## Step 6: Change Directory to the Extracted Folder
- In the Command Prompt or Terminal, type `cd` followed by a space, and **paste the path** you copied.

- Example:
- cd C:\Users\YourName\Downloads\Movie-finder-main
## Step 7: Install the Required Packages
- Paste the following command to install all the dependencies required for the project:
- pip install -r requirements.txt
## Step 8: Run the Application
- To start the application, paste the following command and press Enter:
- python app.py
## Step 9: Open the Application in Your Browser
- Once the server is running, open your web browser and navigate to:
http://127.0.0.1:5000