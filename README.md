# Jokes Automated

**Jokes Automated** is a service that allows you to send jokes automatically to people who fill out a Google Form. This project integrates a joke API with Google Sheets, using a cron job to send jokes to emails collected from the form submissions.

## Demo

You can try the live API [here](https://jokes-automated.vercel.app/).

## Features
- Integrates a joke API to send jokes automatically.
- Links Google Sheets with Google Forms to send jokes to emails from form responses.
- Uses cron jobs to automate the sending process.
- Hosted on Vercel.

## Project Structure
- `api/index.py`: The backend API that handles sending jokes to emails.
- `cron_job.js`: A script that connects the Google Sheets to the cron job functionality using Google Apps Script.
  
## Setup Instructions

### Prerequisites

Before getting started, ensure you have the following:

1. **Python 3.x** (for the backend API)
2. **Node.js and npm** (for running the cron job in Google Sheets)
3. **Google Sheets account** with access to Google Forms.
4. **Vercel account** to deploy the API.

### 1. Clone the Repository

```bash
git clone https://github.com/OjasMittal/jokes_automated.git
cd jokes_automated
```

### 2. Set Up the Backend API
Install the required Python libraries:

```bash
pip install -r requirements.txt
```
Configure the API: Update the .env file with your credentials as in sample .env file for sending jokes.

Deploy the API: You can deploy the API on platforms like Vercel or any other Python-compatible hosting service or use the already deployed one.

### 3. Set Up Google Sheets and Cron Job
Google Sheets Setup:

Create a Google Sheet linked to a Google Form.
Ensure that the form collects emails from users who fill it out.
Install Google Apps Script:

Open the Google Sheets document linked to the form.
In the menu, go to Extensions > Apps Script.
Paste the contents of cron_job.js into the script editor.
Set up the Cron Job:

In the script editor, configure a time-driven trigger to run the cron job at regular intervals.
This script will collect form responses and send the appropriate jokes via the API.
### 4. Running the Cron Job
Once the Google Apps Script is set up, the cron job will trigger automatically according to your configured schedule. It will send an email to all form respondents with a joke.

### Usage
Once everything is set up:

Fill out the Google Form to simulate submissions.
The system will automatically send a joke to the email address provided in the form.
Contributing
Feel free to fork the repository, make changes, and create pull requests for improvements or fixes.

### License
This project is licensed under the MIT License.

