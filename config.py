#Metadata
TOKEN_DESCRIPTION = "An astronaut homie that'll be your best friend."

#location of image assets and where the files will be generated
ASSET_FOLDER = 'assets/'
GENERATED_FOLDER = 'generated/'
METADATA = "metadata/"
TOKENS = "tokens/"
STATISTICS = "statistics/"

FINAL_ATTRIBUTE_VALUES = {
    "background": {
        "Blue": 0,
        "Dusk": 0,
        "Green": 0,
        "Purple": 0,
        "Red": 0,
        "Stars": 0,
        "Sunrise": 0,
        "Yellow": 0
    },
    "jetpack": {
        "Katanas": 0,
        "Scuba Tank": 0,
        "Space O2": 0,
    },
    "human": {
        "Human 1": 0,
        "Human 2": 0,
        "Human 3": 0,
        "Human 4": 0,
        "Human 5": 0,
    },
    "spacesuit": {
        "Accountant": 0,
        "Bathrobe": 0,
        "Bolo Tie": 0,
        "Gondolier": 0,
        "Hoodie": 0,
        "Moonshooters T-shirt": 0,
        "Orange Space Suit": 0,
        "Puffy Coat": 0,
        "Tropical": 0,
        "Turtle Neck": 0,
        "Tuxedo": 0,
        "White Space Suit": 0
    },
    "faceshield": {
        "Alien Splat": 0,
        "Black": 0,
        "Blue": 0,
        "Broken": 0,
        "Duct Taped": 0,
        "Gold": 0,
        "Orange": 0,
        "Purple": 0,
        "Silver": 0,
        "Tie Dye": 0,
    },
    "headwear": {
        "Bucket Hat": 0,
        "Cowboy Hat": 0,
        "Crown": 0,
        "Drink Hat": 0,
        "Hair Buns": 0,
        "Halo": 0,
        "Headphones": 0,
        "Moonshooters Cap": 0,
        "Party Hat": 0,
        "Ponytail": 0,
        "Propellor Hat": 0,
    }
}

# Dictionary of attributes, in order of layer depth (lowest first)
ATTRIBUTES = {
    'jetpack': {  #  The rarity of jetpack is ~15%
        1: 'Katanas', #  Rarity of Katanas is ~20% of all jetpacks
        2: 'Scuba Tank', #  Rarity of Scuba Tank is ~40% of all jetpacks
        3: 'Space O2', #  Rarity of Space O2 is ~40% of all jetpacks
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
        10: '',
        11: '',
        12: '',
        13: '',
        14: '',
        15: '',
        16: 'Scuba Tank',
        17: 'Space O2',
        18: '',
        19: '',
        20: '',
        21: '',
        22: '',
        23: '',
        24: '',
        25: '',
        26: '',
        27: '',
        28: '',
        29: '',
        30: '',
        31: '',
        32: '',
        33: ''
    },
    'human': {
        1: 'Human 1',
        2: 'Human 2',
        3: 'Human 3',
        4: 'Human 4',
        5: 'Human 5',
    },
    'spacesuit': {
        1: 'Accountant',
        2: 'Bathrobe',
        3: 'Bolo Tie',
        4: 'Hoodie',
        5: 'Moonshooters T-Shirt',
        6: 'Orange Space Suit',
        7: 'Tropical',
        8: 'Turtle Neck',
        9: 'Tuxedo',
        10: 'White Space Suit',
        11: 'Puffy Coat',
        12: 'Gondolier',
        13: 'Accountant',
        14: 'Bathrobe',
        15: 'Bolo Tie',
        16: 'Hoodie',
        17: 'Orange Space Suit',
        18: 'Tropical',
        19: 'Turtle Neck',
        20: 'Tuxedo',
        21: 'White Space Suit',
        22: 'Puffy Coat',
        23: 'Gondolier',
        24: 'Accountant',
        25: 'Bathrobe',
        26: 'Bolo Tie',
        27: 'Hoodie',
        28: 'Orange Space Suit',
        29: 'Tropical',
        30: 'Turtle Neck',
        31: 'Tuxedo',
        32: 'White Space Suit',
        33: 'Puffy Coat',
        34: 'Gondolier',
        35: 'Accountant',
        36: 'Bathrobe',
        37: 'Bolo Tie',
        38: 'Hoodie',
        39: 'Orange Space Suit',
        40: 'Tropical',
        41: 'Turtle Neck',
        42: 'Tuxedo',
        43: 'White Space Suit',
        44: 'Puffy Coat',
        45: 'Gondolier',
        46: 'Accountant',
        47: 'Bathrobe',
        48: 'Bolo Tie',
        49: 'Hoodie',
        50: 'Orange Space Suit',
        51: 'Tropical',
        52: 'Turtle Neck',
        53: 'Tuxedo',
        54: 'White Space Suit',
        55: 'Puffy Coat',
        56: 'Gondolier',
        57: 'Accountant',
        58: 'Bathrobe',
        59: 'Bolo Tie',
        60: 'Hoodie',
        61: 'Orange Space Suit',
        62: 'Tropical',
        63: 'Turtle Neck',
        64: 'Tuxedo',
        65: 'White Space Suit',
        66: 'Puffy Coat',
        67: 'Gondolier',
        68: 'Accountant',
        69: 'Bathrobe',
        70: 'Bolo Tie',
        71: 'Hoodie',
        72: 'Orange Space Suit',
        73: 'Tropical',
        74: 'Turtle Neck',
        75: 'Tuxedo',
        76: 'White Space Suit',
        77: 'Puffy Coat',
        78: 'Gondolier',
    },
    'faceshield': { # TODO broken and black should be ultra rare
        1: 'Black', # Rarity of Black is ~15% of all faceshields
        2: 'Blue',  # Rarity of Blue is ~15% of all faceshields
        3: 'Broken', # Rarity of Broken is ~5% of all faceshields
        4: 'Duct Taped', # Rarity of Duct Taped is ~5% of all faceshields
        5: 'Gold', # Rarity of Gold is ~5% of all faceshields
        6: 'Orange', # Rarity of Orange is ~15% of all faceshields
        7: 'Purple', # Rarity of Purple is ~15% of all faceshields
        8: 'Silver', # Rarity of Silver is ~15% of all faceshields
        9: 'Tie Dye', # Rarity of Tie Dye is ~5% of all faceshields
        10: 'Alien Splat', # Rarity of Alien Splat is ~5% of all faceshields
        11: 'Black',
        12: 'Black',
        13: 'Blue',
        14: 'Blue',
        15: 'Orange',
        16: 'Orange',
        17: 'Purple',
        18: 'Purple',
        19: 'Silver',
        20: 'Silver',

    },
    'headwear': { # Rarity of headwear is ~61%
        1: 'Cowboy Hat',
        2: 'Drink Hat',
        3: 'Hair Buns',
        4: 'Halo',
        5: 'Headphones',
        6: 'Moonshooters Cap', # Rarity of Moonshooters Cap is ~2% of all headwear
        7: 'Party Hat',
        8: 'Ponytail',
        9: 'Propellor Hat',
        10: 'Bucket Hat',
        11: 'Crown',
        12: '',
        13: '',
        14: '',
        15: '',
        16: '',
        17: '',
        18: '',
        19: 'Cowboy Hat',
        20: 'Drink Hat',
        21: 'Hair Buns',
        22: 'Halo',
        23: 'Headphones',
        24: 'Party Hat',
        25: 'Ponytail',
        26: 'Propellor Hat',
        27: 'Bucket Hat',
        28: 'Crown',
        29: 'Cowboy Hat',
        30: 'Drink Hat',
        31: 'Hair Buns',
        32: 'Halo',
        33: 'Headphones',
        34: 'Party Hat',
        35: 'Ponytail',
        36: 'Propellor Hat',
        37: 'Bucket Hat',
        38: 'Crown',
        39: '',
        40: '',
        41: '',
        42: '',
        43: '',
        44: '',
        45: '',
        46: '',
        47: '',
        48: '',
        49: '',
        50: '',
    }
}

# Background colors
BACKGROUND = {
    1: 'Blue', # Rarity of Blue is ~16% of all backgrounds
    2: 'Dusk', # Rarity of Dusk is ~5% of all backgrounds
    3: 'Green', # Rarity of Green is ~16% of all backgrounds
    4: 'Purple', # Rarity of Purple is ~16% of all backgrounds
    5: 'Red', # Rarity of Red is ~16% of all backgrounds
    6: 'Stars', # Rarity of Stars is ~5% of all backgrounds
    7: 'Sunrise', # Rarity of Sunrise is ~5% of all backgrounds
    8: 'Yellow', # Rarity of Yellow is ~16% of all backgrounds
    9: 'Blue',
    10: 'Blue',
    11: 'Green',
    12: 'Green',
    13: 'Purple',
    14: 'Purple',
    15: 'Red',
    16: 'Red',
    17: 'Yellow',
    18: 'Yellow',
}