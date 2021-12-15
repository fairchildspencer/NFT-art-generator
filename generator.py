import random
import json
from config import *
from PIL import Image
from pathlib import Path

def generateRandomNumber(min, max):
	return random.randint(min, max)

def generateEthMetaData(tokenID, attributes, bgColor):
	metadata = {}

	metadata["title"] = "Asset Metadata"
	metadata["type"] = "object"

	metadata["properties"] = {}
	metadata["properties"]["name"] = str(tokenID)
	metadata["properties"]["description"] = TOKEN_DESCRIPTION
	metadata["properties"]["image"] = 'url' #needs to be setup later
	metadata["properties"]["background_color"] = bgColor
	metadata["properties"]["attributes"] = []

	for attr in attributes:
		toAdd = {
			"trait_type": attr,
			"value": attributes[attr]
		}
		metadata["properties"]["attributes"].append(toAdd)

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
		img = Image.open(ASSET_FOLDER + layer + "/" + str(attributes[layer]) + '.png').convert("RGBA")
		img = img.resize((IMAGE_X_PIXELS, IMAGE_Y_PIXELS), resample=Image.NEAREST)
		base.paste(img, (0, 0), img)

	return base

def saveToken(token, tokenID, metadata):
	path = Path(GENERATED_FOLDER + str(tokenID) + '.png')
	token.save(path, "PNG")

	with open(GENERATED_FOLDER + str(tokenID) + '.json', 'w') as outfile:
		json.dump(metadata, outfile, indent=4)

def main(generationCount):
	for i in range(generationCount):
		bgColor = generateRandomNumber(1, len(COLORS))
		base = Image.new('RGB', (IMAGE_X_PIXELS, IMAGE_Y_PIXELS), COLORS[bgColor])

		attributeIndices = {}
		metaAttributes = {}

		for attr in ATTRIBUTES:
			attributeIndices[attr] = generateRandomNumber(1, len(ATTRIBUTES[attr]))
			metaAttributes[attr] = ATTRIBUTES[attr][attributeIndices[attr]]


		token = generateImage(base, attributeIndices)

		metadata = {}
		if (METADATA_SCHEMA == "eth"):
			metaData = generateEthMetaData(i, metaAttributes, bgColor)
		elif (METADATA_SCHEMA == "sol"):
			metaData = generateSolMetaData(i, metaAttributes)

		saveToken(token, i, metaData)

main(5)
