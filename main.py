from character_image import picksel
import sys

def main(filepath: str, output_path: str = "output.txt", detailed:bool = True):
    picksel(filepath, output_path = output_path, detailed = detailed)
    
if __name__ == "__main__":
    filepath = sys.argv[1]
    output_path = sys.argv[2]
    detailed = sys.argv[3]
    
    main(filepath, output_path, detailed)