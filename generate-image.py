import sys
import os
import glob
import json
import requests
import replicate


def load_prompt():
    # load JSON
    with open(sys.path[0] + '/data/prompt.json') as json_file:
        json_data = json.load(json_file)
    return json_data["prompt"]


def generate_prediction(prompt):

    previous_images = []
    for file in glob.glob(sys.path[0] + "/images/*.png"):
        previous_images.append(file)

    prediction_generator = replicate.models.get(
        "stability-ai/stable-diffusion").predict(prompt=prompt, width=1024, height=768)

    # iterate over prediction responses
    for index, url in enumerate(prediction_generator):

        # construct filename
        uuid = url.split('/')[-2]
        extension = url.split('.')[-1]  # jpg, png, etc
        filename = f"/images/{uuid}.{extension}"

        # download and save the file
        data = requests.get(url)
        with open(sys.path[0] + filename, 'wb') as file:
            file.write(data.content)

    for file in previous_images:
        os.remove(file)


prompt = load_prompt()
generate_prediction(prompt)
