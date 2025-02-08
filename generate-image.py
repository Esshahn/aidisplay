import sys
import os
import glob
import json
import requests
import replicate


def load_prompt():
    """Load the JSON prompt from file."""
    filepath = os.path.join(sys.path[0], 'data/prompt.json')
    with open(filepath, 'r') as json_file:
        return json.load(json_file)["prompt"]


def generate_prediction(prompt):
    """Generate an image prediction and save it to the 'images' folder."""

    # Ensure the 'images' folder exists
    images_folder = os.path.join(sys.path[0], "images")
    os.makedirs(images_folder, exist_ok=True)

    # Store previous images for cleanup
    previous_images = glob.glob(os.path.join(images_folder, "*.png"))

    inputs = {
        'prompt': prompt,
        'width': 1024,
        'height': 640
    }

    versions = [
        "f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1",
        "ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4"
    ]

    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get(versions[1])

    prediction_generator = version.predict(**inputs)

    # Iterate over prediction responses
    for index, url in enumerate(prediction_generator):
        uuid = url.split('/')[-2]
        extension = url.split('.')[-1]  # jpg, png, etc.
        filename = os.path.join(images_folder, f"{uuid}.{extension}")

        # Download and save the image
        data = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(data.content)

    # Remove old images
    for file in previous_images:
        os.remove(file)


# Run the script
prompt = load_prompt()
generate_prediction(prompt)