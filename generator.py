import random
import json
from config import *
from PIL import Image
from pathlib import Path

ASSETFOLDER = 'assets/'
GENERATEDFOLDER = 'generated/'

def generateRandomNumber(min, max):
    return random.randint(min, max)

def createBodyDict():
    bodyDict = {
        1: 'ghost',
        2: 'mario',
        3: 'megaman'
    }
    return bodyDict

def createExtraDict():
    extraDict = {
        1: 'heart',
        2: 'pizza',
        3: 'block'
    }
    return extraDict

def createColorDict():
    colorDict = {
        1: (228, 150, 150),
        2: (150, 228, 150),
        3: (150, 150, 228)
    }
    return colorDict

def generateMetaData(tokenID, attributes):
    metadata = {}
    metadata["name"] = str(tokenID)
    metadata["description"] = 'Description of item'
    metadata["image"] = 'url'
    metadata["background_color"] = 'color'
    metadata["attributes"] = []
    metadata["attributes"].append(
    {
        "trait_type": "body",
        "value": attributes["body"]
    })
    metadata["attributes"].append(
    {
        "trait_type": "extra",
        "value": attributes["extra"]
    })
    return metadata

def generateImage(base, attributes):
    img0 = Image.open(ASSETFOLDER + "body/" + str(attributes['body']) + ".png").convert("RGBA")
    img0 = img0.resize((600, 600), resample=Image.NEAREST)
    img1 = Image.open(ASSETFOLDER + "extra/" + str(attributes['extra']) + ".png").convert("RGBA")
    img1 = img1.resize((200, 200), resample=Image.NEAREST)

    base.paste(img0, (0, 0), img0)
    base.paste(img1, (60, 260), img1)

    return base

def saveToken(token, tokenID, metadata):
    path = Path(GENERATEDFOLDER + str(tokenID) + '.png')
    token.save(path, "PNG")

    with open(GENERATEDFOLDER + str(tokenID) + '.json', 'w') as outfile:
        json.dump(metadata, outfile, indent=4)

def main(generationCount):
    bodyDict = createBodyDict()
    extraDict = createExtraDict()
    colorDict = createColorDict()
    
    for i in range(generationCount):
        base = Image.new('RGB', (600, 600), colorDict[generateRandomNumber(1, 3)])
        body = generateRandomNumber(1, 1)
        extra = generateRandomNumber(1, 3)

        generationAtr = {
            "body": body,
            "extra": extra
        }

        metaAtr = {
            "body": bodyDict[body],
            "extra": extraDict[extra]
        }

        token = generateImage(base, generationAtr) # TODO - change this function to use the config file
        metaData = generateMetaData(i, metaAtr)

        saveToken(token, i, metaData)

main(5)
