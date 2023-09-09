## aidisplay

- Reads the current weather at a given location
- transforms weather information into a prompt for replicate
- queries replicate with prompt and downloads image
- displays image

## Setup
- get an API token from replicate.com

- use a desktop based normal raspbian distro
- make sure to have ssh and wifi setup during image creation
- git is already installed, so `git pull` the repo into `pi/Code/``

- install `replicate` via `pip install replicate`
- install `feh` image viewer with `sudo apt install feh -y`

edit profile with `sudo nano /etc/profile`
at the end of the file, add

```
export REPLICATE_API_TOKEN=<API TOKEN> 
feh -F --zoom fill -D10 -R10 /home/pi/Code/aidisplay/images/
```

This instructs feh to fill the whole display with the image, and check every 10 seconds for new images (R) and display them for ten seconds (D). The API Token is not needed for the script to execute fine, but is convenient when you have to manually execute a script to test if it works.

Setup a the cron jobs. For this, enter `crontab -e` and add these lines:

```
0 7-20/3 * * * REPLICATE_API_TOKEN=<API TOKEN> /home/pi/Code/aidisplay/cron.sh >> /home/pi/Code/aidisplay/log.txt >2&1
```

- runs every 3 hours until 20:00, starting at 7, then 9, 11...
- saves all text output in a log file
- for testing purposes, you might want to check on a shorter interval, e.g. five minutes: `*/5 * * * *`

Next, edit the root crontab (for shutdown privileges), enter `sudo crontab -e` and add this line:

```
00 21 * * * sudo shutdown
```

- shuts down the system every day at 21  


## RUN

reboot system with `sudo reboot` and you should be done.



