import cv2
import numpy as np

def read_image(filepath: str) -> np.ndarray:
    return cv2.cvtColor(cv2.imread(filepath), cv2.COLOR_BGR2GRAY)

def grayscale_character_helper(detailed: bool = True) -> dict:
    grayscale_char = {}

    increment = 3.642857142857143 if detailed else 25.5
    offset = 0.000000000000001 if detailed else .1
    
    char_list = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")[::-1] if detailed else list(" .:-=+*#%@")

    for i in np.arange(0.0, 255.0, increment):
        char_key = str(char_list[round(i / increment)] + ' ')
        
        grayscale_char[char_key] = (float(i), float(i + increment)) if i == 0.0 else (float(i + offset), float(i + increment))
            
    return grayscale_char

def picksel(image, grayscale_characters, output_path: str):
    cache = {}

    with open(output_path, "w") as f:
        for row in image:
            for col in row:
                if col in cache:
                    f.write(cache[col])
                    
                else:
                    for key, value in grayscale_characters.items():
                        if value[0] <= col < value[1]:
                            cache[col] = key
                            f.write(key)          
                            
            f.write("\n")
            
