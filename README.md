## aidisplay

- Reads the current weather at a given location
- transforms weather information into a prompt for replicate
- queries replicate with prompt and downloads image
- displays image

## Setup

- install `replicate` via `pip install replicate`
- install `fbi` image viewer with `sudo apt-get install fbi`
- export your replicate API TOKEN `export REPLICATE_API_TOKEN=<API_TOKEN>`

## Run

First you setup a cron job. For this, enter `crontab -e` and add these lines:

```
*/30 * * * * python3 /home/pi/code/aidisplay/cron.sh
```

This will execute every 30 minutes and

- get the weather
- generate an image
