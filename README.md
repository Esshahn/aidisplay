## aidisplay

- Reads the current weather at a given location
- transforms weather information into a prompt for replicate
- queries replicate with prompt and downloads image
- displays image

## Setup

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

This instructs feh to fill the whole display with the image, and check every 10 minutes for new images (D) and display them for ten minutes (R).

Setup a cron job. For this, enter `crontab -e` and add these lines:

```
0 7-20/2,8 * * 0,6 /bin/bash /home/pi/Code/aidisplay/cron.sh
0 21 * * * /sbin/shutdown -h now
```

- runs every 2 hours
- first at 7, last at 20
- saturday & sunday starts at 8
- shuts down the system every day at 21  


