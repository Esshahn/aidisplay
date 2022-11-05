## aidisplay

- Reads the current weather at a given location
- transforms weather information into a prompt for replicate
- queries replicate with prompt and downloads image
- displays image

## Setup

- install `replicate` via `pip install replicate`
- install `feh` image viewer with `sudo apt install feh -y`
- export your replicate API TOKEN `export REPLICATE_API_TOKEN=<API_TOKEN>`

## Run

First you setup a cron job. For this, enter `crontab -e` and add these lines:

```
*/30 * * * * python3 /home/pi/code/aidisplay/cron.sh
```

This will execute every 30 minutes and

- get the weather
- generate an image

chmod +x display-image.sh

sudo nano /etc/profile
export REPLICATE_API_TOKEN=3b534893471c8f85e3e8abfff549342db9a99caf
feh -F -Z -D4 -R2 /home/pi/Pictures/



* 12 * * * REPLICATE_API_TOKEN=3b534893471c8f85e3e8abfff549342db9a99caf /home/pi/code/aidisplay/cron.sh
*/6 * * * * DISPLAY=:0 /home/pi/code/aidisplay/display-image.sh

---

Normale PI Distro MIT Desktop
FEH installieren (3.6.1 ist okay)
feh -F -Z -D4 -R2 /home/pi/Pictures/
Lädt alle Bilder aus dem Ordner, zeigt jedes 4 Sekunden an und macht alle 2 Sekunden einen Reload des Ordnerinhaltes

