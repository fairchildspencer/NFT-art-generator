import random
import json
from config import *
from PIL import Image
from pathlib import Path

def generateRandomNumber(min, max):
	return random.randint(min, max)

def generateEthMetaData(tokenID, attributes, bg):
	metadata = {}

	metadata["name"] = str(tokenID)
	metadata["description"] = TOKEN_DESCRIPTION
	metadata["image"] = 'url' #needs to be setup later
	metadata["attributes"] = []

	bgColor = {
		"trait_type": "background",
		"value": BACKGROUND[bg]
	}
	metadata["attributes"].append(bgColor)

	for attr in attributes:
		if (attributes[attr] != ""):
			toAdd = {
				"trait_type": attr,
				"value": attributes[attr]
			}
			metadata["attributes"].append(toAdd)

	return metadata

def generateImage(bg, currentAtrs):
	base = Image.open(ASSET_FOLDER + 'background/' + BACKGROUND[bg] + '.png')
	FINAL_ATTRIBUTE_VALUES["background"][BACKGROUND[bg]] += 1
	for layer in ATTRIBUTES:
		if (currentAtrs[layer] == ''):  # skip the layer if the random number is out of range
			continue

		FINAL_ATTRIBUTE_VALUES[layer][currentAtrs[layer]] += 1

		img = Image.open(ASSET_FOLDER + layer + "/" + currentAtrs[layer] + '.png')
		base.paste(img, (0, 0), img)

	return base

def saveToken(token, tokenID, metadata):
	path = Path(GENERATED_FOLDER + TOKENS + str(tokenID) + '.png')
	token.save(path, "PNG")

	with open(GENERATED_FOLDER + METADATA + str(tokenID) + '.json', 'w') as outfile:
		json.dump(metadata, outfile, indent=4)

def saveFinalAttributeValues():
	with open(GENERATED_FOLDER + STATISTICS + 'final_attribute_values.json', 'w') as outfile:
		json.dump(FINAL_ATTRIBUTE_VALUES, outfile, indent=4)

def main(generationCount):
	for i in range(generationCount):
		metaAttributes = {}

		for attr in ATTRIBUTES:
			metaAttributes[attr] = ATTRIBUTES[attr][generateRandomNumber(1, len(ATTRIBUTES[attr]))]

		bg = generateRandomNumber(1, len(BACKGROUND))
		token = generateImage(bg, metaAttributes)

		metaData = generateEthMetaData(i, metaAttributes, bg)

		saveToken(token, i, metaData)
		saveFinalAttributeValues()

main(5)
