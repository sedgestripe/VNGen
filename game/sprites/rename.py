import os

lineart = [
    ["kit1", "kit2", "kit3"],
    ["app1", "app2", "app3"],
    ["short1", "short2", "short3"],
    ["long1", "long2", "long3"],
    ["elder1", "elder2", "elder3"],
    ["para1", "para2", "para3"]
]

base_colors = [['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'HALF', 'STREAK', 'MASK', 'SMOKE'],['MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'SWOOP', 'CHIMERA', 'CHEST', 'ARMTAIL', 'GRUMPYFACE'],['MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'SMUDGED', 'DAUB', 'EMBER', 'BRIE'],['ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'DAPPLENIGHT', 'BLANKET', 'BELOVED']]

def rename_images_in_directory(directory):
    
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Sort image files for consistent renaming
    
    index = 0  # Keep track of the image file we're renaming
    
    # Loop through base colors and lineart to rename files
    for colors in base_colors:
        for art in lineart:
            for color in colors:
                for lines in art:
                    old_name = os.path.join(directory, image_files[index])
                    print(old_name)
                    new_name = os.path.join(directory, f"{lines}-{color}.png")  # Using .png, modify if different format needed
                    os.rename(old_name, new_name)
                    index += 1

if __name__ == "__main__":
    directory = "game\sprites\TortiePatches copy"
    rename_images_in_directory(directory)
