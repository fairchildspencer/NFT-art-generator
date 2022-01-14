#Metadata schema
METADATA_SCHEMA = "eth"
TOKEN_DESCRIPTION = "An astronaut homie that'll be your best friend."

#Sol only metadata attributes
COLLECTION_NAME = "MoonShooters"
COLLECTION_SYMBOL = "MS"
SELLER_FEE = 1000
OWNER_1_ADDRESS = "0x0000000000000000000000000000000000000000"
OWNER_2_ADDRESS = "0x0000000000000000000000000000000000000000"

#Image size
IMAGE_X_PIXELS = 350
IMAGE_Y_PIXELS = 350

#location of image assets and where the files will be generated
ASSET_FOLDER = 'assets/'
GENERATED_FOLDER = 'generated/'

# Dictionary of attributes, in order of layer depth (lowest first)
ATTRIBUTES = {
    'body': {
        1: 'ghost', # If you want an attribute to be optional, add blank attributes to the dictionary
    },
    'extra': {
        1: 'heart',
        2: 'pizza',
        3: 'block',
        4: ''
    }
}

# Color dictionary is required
COLORS = {
    1: (228, 150, 150),
    2: (150, 228, 150),
    3: (150, 150, 228)
}