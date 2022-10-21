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

- `python3 get-weather.py`
- `python3 generate-image.py`
- 