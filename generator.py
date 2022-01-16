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

def generateSolMetaData(tokenID, attributes):
	metadata = {}

	metadata["name"] = str(tokenID)
	metadata["description"] = TOKEN_DESCRIPTION
	metadata["symbol"] = COLLECTION_SYMBOL
	metadata["image"] = 'uri' #needs to be setup later
	metadata["seller_fee_basis_points"] = SELLER_FEE

	metadata["collection"] = {
		"name": COLLECTION_NAME,
	}

	metadata["properties"] = {}
	metadata["properties"]["category"] = "image"
	metadata["properties"]["creators"] = [
		{
        	"address": OWNER_1_ADDRESS,
        	"share": 50
      	},
		{
        	"address": OWNER_2_ADDRESS,
        	"share": 50
      	}
	]

	metadata["attributes"] = []
	for attr in attributes:
		toAdd = {
			"trait_type": attr,
			"value": attributes[attr]
		}
		metadata["attributes"].append(toAdd)

	return metadata

def generateImage(base, attributes):
	for layer in ATTRIBUTES:
		if (ATTRIBUTES[layer][attributes[layer]] == ''):  # skip the layer if the random number is out of range
			continue

		img = Image.open(ASSET_FOLDER + layer + "/" + str(attributes[layer]) + '.png')
		base.paste(img, (0, 0), img)

	return base

def saveToken(token, tokenID, metadata):
	path = Path(GENERATED_FOLDER + str(tokenID) + '.png')
	token.save(path, "PNG")

	with open(GENERATED_FOLDER + str(tokenID) + '.json', 'w') as outfile:
		json.dump(metadata, outfile, indent=4)

def main(generationCount):
	for i in range(generationCount):
		bg = generateRandomNumber(1, len(BACKGROUND))
		base = Image.open(ASSET_FOLDER + 'background/' + str(bg) + '.png')

		attributeIndices = {}
		metaAttributes = {}

		for attr in ATTRIBUTES:
			attributeIndices[attr] = generateRandomNumber(1, len(ATTRIBUTES[attr]))
			metaAttributes[attr] = ATTRIBUTES[attr][attributeIndices[attr]]


		token = generateImage(base, attributeIndices)

		metadata = {}
		if (METADATA_SCHEMA == "eth"):
			metaData = generateEthMetaData(i, metaAttributes, bg)
		elif (METADATA_SCHEMA == "sol"):
			metaData = generateSolMetaData(i, metaAttributes)

		saveToken(token, i, metaData)

main(30)
