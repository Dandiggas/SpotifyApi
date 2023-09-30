# Spotify New Music Friday Emailer

## Overview
This automated script sends a curated email containing the latest tracks and artists from Spotify's 'New Music Friday' playlist to my inbox every Friday at 8 AM.

## Features
- **Automated Emailing**: The script automatically sends an email every Friday at 8 AM.
- **Data Retrieval**: Retrieves the latest tracks and artists from Spotify's 'New Music Friday'.
  
## Technologies and Tools Learned
- **SMTP**: Used for sending emails programmatically.
- **Spotify API**: Utilized to retrieve playlist information.
- **Cron Jobs**: Scheduled the script to run at specific times.
- **Requests Library**: Used for making HTTP requests to the Spotify API.

## Requirements
- Python 3.x
- A Spotify Developer Account
- SMTP Enabled Email Account

## Setup
1. Clone the repo: `git clone https://github.com/Dandiggas/SpotifyApi`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environmental variables for email and password.
4. Schedule the script using Cron Jobs (Linux/Mac) or Task Scheduler (Windows).

### Scheduling with Cron
Open your terminal and type `crontab -e` to edit your cron jobs.

Add the following line to schedule the script to run every Friday at 8 AM:

0 8 * * 5 cd /path/to/your/script && /usr/bin/python3 main.py

## Usage
Run `python main.py` to manually execute the script, or let the cron job handle the scheduled tasks.

## Author
Daniel Adekugbe 

