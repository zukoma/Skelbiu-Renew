# Skelbiu-Renew
Renew skelbiu.lt ads with headless web driver.

# Requirements
- Selenium
- Chrome Driver

# Getting started

Change username and password field and adjust path to the web driver. Once filled in:

```bash
pip install -r requirements.txt
chmod +x Skelbiu.py
./Skelbiu.py username password
```
# For RPI
- sudo apt-get install chromium-chromedriver
- Change path to: /usr/lib/chromium-browser/chromedriver

# Set Chronetab for daily run
- crontab -e
- "* 18 * * * /home/pi/skelbiu.lt.py" (will run everyday at 6pm)


