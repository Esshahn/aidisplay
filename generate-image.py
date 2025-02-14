import sys
import os
import json
import requests
import replicate

def load_prompt():
    """Load the JSON prompt from file."""
    filepath = os.path.join(sys.path[0], 'data/prompt.json')
    with open(filepath, 'r') as json_file:
        return json.load(json_file)["prompt"]

def generate_prediction(prompt):
    """
    Generate an image prediction and save it to the 'images' folder atomically.
    Instead of deleting old files, we always update the same file (current.png).
    """
    images_folder = os.path.join(sys.path[0], "images")
    os.makedirs(images_folder, exist_ok=True)
    
    # This will be the file that feh displays
    final_filename = os.path.join(images_folder, "current.png")
    
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
    prediction_result = version.predict(**inputs)
    
    # Since prediction_result is a list, we access the first element.
    if not prediction_result:
        print("No image URL received.")
        return
    url = prediction_result[0]
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to download image.")
        return
    
    # Write to a temporary file first
    tmp_filename = os.path.join(images_folder, "current.tmp")
    with open(tmp_filename, 'wb') as file:
        file.write(response.content)
    
    # Atomically replace the old image with the new one
    os.replace(tmp_filename, final_filename)

# Run the script
prompt = load_prompt()
generate_prediction(prompt)
