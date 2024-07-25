IMAP Web Trigger

Setup Instructions
1. Clone the Repository
Clone this repository to your local machine.

2. Update Credentials
Update the credentials in the .env file.

3. Install Requirements
Install the required packages listed in requirements.txt:

pip install -r requirements.txt

4. Schedule the Script

Schedule the script to run every minute. Add the following line to your crontab:

* * * * * /home/ubuntu/imap-web-trigger/env/bin/python3 /home/ubuntu/imap-web-trigger/script.py >> imap.log 2>&1
