import sys
import json
import requests
import replicate


def load_prompt():
    # load JSON
    with open(sys.path[0] + '/data/prompt.json') as json_file:
        json_data = json.load(json_file)
    return json_data["prompt"]


def generate_prediction(prompt):
    prediction_generator = replicate.models.get(
        "stability-ai/stable-diffusion").predict(prompt=prompt)

    # iterate over prediction responses
    for index, url in enumerate(prediction_generator):

        # construct filename
        uuid = url.split('/')[-2]
        extension = url.split('.')[-1]  # jpg, png, etc
        filename = f"images/{uuid}.{extension}"

        # download and save the file
        data = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(data.content)

    filename_JSON = {
        "filename": filename
    }
    with open("data/filename.json", 'w') as file_object:
        json.dump(filename_JSON, file_object)


prompt = load_prompt()
generate_prediction(prompt)
