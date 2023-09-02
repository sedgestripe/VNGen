from PIL import Image
import os

def is_blank_or_transparent(image_path):
    """
    Check if the image is blank or transparent.
    Returns True if it is, False otherwise.
    """
    with Image.open(image_path) as img:
        img = img.convert("RGBA")
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b, a = img.getpixel((x, y))
                if a != 0:  # Check if pixel is not transparent
                    return False
    return True

def delete_blank_or_transparent_images(folder_path):
    """
    Delete all blank or transparent images from the specified folder.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                if is_blank_or_transparent(image_path):
                    os.remove(image_path)
                    print(f"Deleted {image_path}")

if __name__ == "__main__":
    # Replace with your directory
    directory = "game\sprites"
    delete_blank_or_transparent_images(directory)
