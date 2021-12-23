##File Renaming

import re
import os
import argparse
from pathlib import Path

def main(showName, test, folder):

    hasChosenNumberInput = False
    chosenNumeric = 0
    
    for count, filename in enumerate(os.listdir()):
        #File Extension
        name, extension = os.path.splitext(filename)

        if filename == "rename.py":
            continue

        #EpisodeNumber
        #foundNumber = re.findall(r'\b\d+\b', filename)#found first? was stricter
        foundNumber = re.findall(r'\d+', filename)
        

        if not foundNumber:
            print(f"No Episode Number found; {filename}")
            continue
        if len(foundNumber) > 1 and not hasChosenNumberInput:
            print(f"Multiple options for episode number; {filename}")
            print(foundNumber)
            for count, number in enumerate(foundNumber):
                print(f"{count} : {number}")
            try:
                chosenNumeric = int(input('Chose which number to use:'))
                hasChosenNumberInput = True
            except ValueError:
                print("Numeric input")
        
        episodeNumber = foundNumber[chosenNumeric].zfill(3)
        
        newName = f"{showName}{episodeNumber}{extension}"
        src: str = f"{folder}/{filename}" 
        dst: str = f"{folder}/{newName}"
        
        print(f"Source: {src}")
        print(f"Destination: {dst}")

        if not test:
            os.rename(Path(src), Path(dst))            
 
# Driver Code
if __name__ == '__main__':
     
    parser = argparse.ArgumentParser(description='Input --name="Shows name" and optionally --test=True to test output first')
    parser.add_argument("--test", type=bool, default=False)
    parser.add_argument("--name", type=str)
    args = parser.parse_args()

    folder = os.path.abspath(os.getcwd())

    print(f"Test: {args.test}")
    print(f"File name: {args.name}")
    print(f"Current Directory: {folder}")

    main(args.name, args.test, folder)
