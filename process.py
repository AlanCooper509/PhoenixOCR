# imports
from easyocr import Reader
import os

# local imports
from ChartTextBoxes import ChartTextBoxes
from enums import Player
from PlayerTextBoxes import PlayerTextBoxes

def cropImage(inputImage, playerTextBox):
    return inputImage[playerTextBox.NW.y:playerTextBox.SE.y, playerTextBox.NW.x:playerTextBox.SE.x]

def runOCR(input_image, debug=False):
    """
    OCR the input image using EasyOCR
    """
    if debug:
        print(f"[INFO] {os.path.basename(__file__)}: OCR'ing input image...")
    reader = Reader(['en'], gpu=True)
    results = reader.readtext(input_image)
    if debug:
        print(f"[INFO] {os.path.basename(__file__)}: {results}")
    return results

def ocrAsInt(ocrResults):
    """
    parse to Int the top-left most (first) text entry returned from running easyOCR on some input image
    """
    try:
        return int(ocrResults[0][1].replace(' ', '').replace('o', '0').replace('O', '0'))
    except:
        return None

def ocrAsIntList(ocrResults):
    """
    parse all as Int the entire list of text entries returned from running easyOCR on some input image
    """
    results = []
    for result in ocrResults:
        results.append(ocrAsInt([result]))
    return results

def mapBreakdownToPlayer(inputListOfSizeSix, dictToAppendTo):
    if len(inputListOfSizeSix) == 6:
        dictToAppendTo["Perfect"]  = inputListOfSizeSix[0]
        dictToAppendTo["Great"]    = inputListOfSizeSix[1]
        dictToAppendTo["Good"]     = inputListOfSizeSix[2]
        dictToAppendTo["Bad"]      = inputListOfSizeSix[3]
        dictToAppendTo["Miss"]     = inputListOfSizeSix[4]
        dictToAppendTo["MaxCombo"] = inputListOfSizeSix[5]


def run(image, mode, debug=False):
    p1 = {}
    p2 = {}

    p1TextBoxes = PlayerTextBoxes(image, Player.P1)
    p2TextBoxes = PlayerTextBoxes(image, Player.P2)

    # get scores for P1 and P2
    p1ScoreImage = cropImage(image, p1TextBoxes.score)
    p1ScoreTextRaw = runOCR(p1ScoreImage, debug)
    p1ScoreText = ocrAsInt(p1ScoreTextRaw)
    p1["Score"] = p1ScoreText

    p2ScoreImage = cropImage(image, p2TextBoxes.score)
    p2ScoreTextRaw = runOCR(p2ScoreImage, debug)
    p2ScoreText = ocrAsInt(p2ScoreTextRaw)
    p2["Score"] = p2ScoreText

    if mode == mode.SCORES:
        return {
            "P1": p1,
            "P2": p2
        }

    # get breakdown (judgement counts and combo) for P1 and P2
    p1BreakdownImage = cropImage(image, p1TextBoxes.breakdown)
    p1BreakdownTextRaw = runOCR(p1BreakdownImage, debug)
    p1BreakdownText = ocrAsIntList(p1BreakdownTextRaw)
    mapBreakdownToPlayer(p1BreakdownText, p1)

    p2BreakdownImage = cropImage(image, p2TextBoxes.breakdown)
    p2BreakdownTextRaw = runOCR(p2BreakdownImage, debug)
    p2BreakdownText = ocrAsIntList(p2BreakdownTextRaw)
    mapBreakdownToPlayer(p2BreakdownText, p2)

    if mode == mode.FAST:
        return {
            "P1": p1,
            "P2": p2
        }
    if mode == mode.ALL:
        chartTextBoxes = ChartTextBoxes(image)
        p1ScoreImage = cropImage(image, p1TextBoxes.score)
        p1ScoreText = int(runOCR(p1ScoreImage, debug)[0][1].replace(' ', ''))
        print(f"[ERROR] {os.path.basename(__file__)}: Not Yet Implemented")