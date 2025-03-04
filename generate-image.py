import os
import json
import requests
import replicate

def generate_image():
    """Generate an AI image from prompt and save it."""
    # Load prompt
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, 'data/prompt.json')) as f:
        prompt = json.load(f)["prompt"]
    
    # Setup paths
    images_dir = os.path.join(script_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    final_path = os.path.join(images_dir, "current.png")
    temp_path = os.path.join(images_dir, "current.tmp")
    
    # Generate image
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4")
    
    result = version.predict(
        prompt=prompt,
        width=1024,
        height=640
    )
    
    # Download and save image
    if not result:
        return print("No image URL received.")
        
    response = requests.get(result[0])
    if response.status_code != 200:
        return print("Failed to download image.")
    
    # Save atomically
    with open(temp_path, 'wb') as f:
        f.write(response.content)
    os.replace(temp_path, final_path)

if __name__ == "__main__":
    generate_image()
