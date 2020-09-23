# Skelbiu-Renew
Renew skelbiu.lt ads with headless web driver.

# Requirements
- Selenium
- Chrome Driver

# Getting started

Change username and password field and fill in path to web driver. Once filled in:

```bash
python skelbiu.py
```
# For Raspberry Pi
sudo apt-get install chromium-chromedriver
Change path to: /usr/lib/chromium-browser/chromedriver

# Set Chronetab for daily run
crontab -e
* 18 * * * /home/pi/skelbiu.lt.py
