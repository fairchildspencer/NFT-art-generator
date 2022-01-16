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
    'jetpack': {
        1: 'katanas',
        2: 'scuba tank',
        3: 'space O2',
        4: '',
        5: '',
        6: '',
        7: '',
    },
    'human': {
        1: 'human 1',
        2: 'human 2',
        3: 'human 3',
        4: 'human 4',
        5: 'human 5',
    },
    'spacesuit': {
        1: 'accountant',
        2: 'bathrobe',
        3: 'bolo tie',
        4: 'hoodie',
        5: 'moonshooters t-shirt',
        6: 'orange space suit',
        7: 'tropical',
        8: 'turtle neck',
        9: 'tuxedo',
        10: 'white space suit',
    },
    'faceshield': {
        1: 'black',
        2: 'blue',
        3: 'broken',
        4: 'duct taped',
        5: 'gold',
        6: 'orange',
        7: 'purple',
        8: 'silver'
    },
    'headwear': {
        1: 'cowboy hat',
        2: 'drink hat',
        3: 'hair buns',
        4: 'halo',
        5: 'headphones',
        6: 'moonshooters cap',
        7: 'party hat',
        8: 'ponytail',
        9: '',
        10: '',
        11: '',
        12: '',
        13: '',
        14: '',
        15: '',
        16: '',
    }
}

# Background colors
BACKGROUND = {
    1: 'blue',
    2: 'dusk',
    3: 'green',
    4: 'purple',
    5: 'red',
    6: 'stars',
    7: 'sunrise',
    8: 'yellow'
}