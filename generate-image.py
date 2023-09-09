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

    inputs = {
        'prompt': prompt,
        'width': 1024,
        'height': 640
    }

    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get(
        "f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1")

    prediction_generator = version.predict(**inputs)

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
