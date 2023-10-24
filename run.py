# !pip install easyocr

# imports
import os
import sys

# local imports
from enums import Modes
import params as p
import postprocess
import preprocess
import process

def main(file_path, mode=Modes.SCORES, url=False, writeToFile=False, outDir="outputs", debug=False):
    input_image = preprocess.load_image(file_path, url)
    if input_image is None: return

    filtered = preprocess.filter_image(input_image)
    outputs = process.run(filtered, mode, debug)
    return postprocess.output(outputs, writeToFile, outDir)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print(f"{p.ERROR_PREFIX(os.path.basename(__file__))} image path was not passed in.")
    elif len(args) == 1:
        main(args[0], mode=Modes.SCORES, url=False, debug=False)
    elif len(args) > 1:
        url = False
        debug = False
        writeToFile = False
        mode = Modes.SCORES
        outDir = "outputs"

        if "-u" in args:
            url = True
            args = [i for i in args if i != "-u"]
        if "-d" in args:
            debug = True
            args = [i for i in args if i != "-d"]
        if "-w" in args:
            writeToFile = True
            args = [i for i in args if i != "-w"]
        if "--mode" in args:
            nextptr = args.index("--mode") + 1
            if nextptr >= len(args):
                print(f"{p.ERROR_PREFIX(os.path.basename(__file__))} missing mode speicifer after '--mode'")
            elif args[nextptr] not in [mode.value for mode in Modes]:
                print(f"{p.ERROR_PREFIX(os.path.basename(__file__))} invalid mode found after '--mode': {args[nextptr]}")
            else:
                mode = Modes(args[nextptr])
                args = [i for i in args if i != "--mode" and i not in [mode.value for mode in Modes]]
        if "--outDir" in args:
            nextptr = args.index("--outDir") + 1
            if nextptr >= len(args):
                print(f"{p.ERROR_PREFIX(os.path.basename(__file__))} missing output dir after '-outDir' arg")
            else:
                outDir = args[nextptr]
                args.pop(nextptr)
                args = [i for i in args if i != "--outDir" and i not in [mode.value for mode in Modes]]
        if len(args) > 1:
            print(f"{p.ERROR_PREFIX(os.path.basename(__file__))} too many unresolved inputs: {args}")
        else:
            main(args[0], mode=mode, url=url, writeToFile=writeToFile, outDir=outDir, debug=debug)