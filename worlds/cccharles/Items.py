from BaseClasses import Item
from .BaseID import base_id


class CCCharlesItem(Item):
    game = "Choo-Choo Charles"


optional_items = {
    "Scraps": base_id + 1,
    "30 Scraps Reward": base_id + 2,
    "25 Scraps Reward": base_id + 3,
    "35 Scraps Reward": base_id + 4,
    "40 Scraps Reward": base_id + 5,
    "South Mine Key": base_id + 6,
    "North Mine Key": base_id + 7,
    "Mountain Ruin Key": base_id + 8,
    "Barn Key": base_id + 9,
    "Candice's Key": base_id + 10,
    "Dead Fish": base_id + 11,
    "Lockpicks": base_id + 12,
    "Ancient Tablet": base_id + 13,
    "Blue Box": base_id + 14,
    "Page Drawing": base_id + 15,
    "Journal": base_id + 16,
    "Timed Dynamite": base_id + 17,
    "Box of Rockets": base_id + 18,
    "Breaker": base_id + 19,
    "Broken Bob": base_id + 20,
    "Employment Contracts": base_id + 21,
    "Mob Camp Key": base_id + 22,
    "Jar of Pickles": base_id + 23,
    "Track Switch Pack": base_id + 44,
    "Track Switch - Barn or Tutorial": base_id + 45, # RailDirectionSwitcher9_26
    "Track Switch - Middle or Port": base_id + 46, # RailDirectionSwitcher7_20
    "Track Switch - Haunted or East": base_id + 47, # RailDirectionSwitcher6_17
    "Track Switch - North or Temple": base_id + 48, # RailDirectionSwitcher5_14
    "Track Switch - Caravan or Cultists": base_id + 49, # RailDirectionSwitcher2_5
    "Track Switch - Camp or Elevator": base_id + 50, # RailDirectionSwitcher3_8
    "Track Switch - Ruin or Temple": base_id + 51, # RailDirectionSwitcher4_11
    "Speed Unlock": base_id + 87,
    "Damage Unlock": base_id + 88,
    "Armor Unlock": base_id + 89,
    "Speed Level": base_id + 90,
    "Damage Level": base_id + 91,
    "Armor Level": base_id + 92
}

useless_items = {
    "Orange Paint Can": base_id + 24,
    "Green Paint Can": base_id + 25,
    "White Paint Can": base_id + 26,
    "Pink Paint Can": base_id + 27,
    "Grey Paint Can": base_id + 28,
    "Blue Paint Can": base_id + 29,
    "Black Paint Can": base_id + 30,
    "Lime Paint Can": base_id + 31,
    "Teal Paint Can": base_id + 32,
    "Red Paint Can": base_id + 33,
    "Purple Paint Can": base_id + 34,
    "The Boomer": base_id + 35,
    "Bob": base_id + 36
}

progression_items = {
    "Green Egg": base_id + 37,
    "Blue Egg": base_id + 38,
    "Red Egg": base_id + 39,
    "Remote Explosive": base_id + 40,
    "Remote Explosive x8": base_id + 41, # Originally, Paul gives 8 explosives at once
    "Temple Key": base_id + 42,
    "Bug Spray": base_id + 43, # Should only be considered progressive in Nightmare Mode
    # Extra progression items
    "Fogbane Relic Pack": base_id + 52,
    "Fogbane Relic - Mine Shaft": base_id + 53,
    "Fogbane Relic - Junkyard Area": base_id + 54,
    "Fogbane Relic - Junkyard Shed": base_id + 55,
    "Fogbane Relic - South House": base_id + 56,
    "Fogbane Relic - Military Base": base_id + 57,
    "Fogbane Relic - South Mine Outside": base_id + 58,
    "Fogbane Relic - Middle Station": base_id + 59,
    "Fogbane Relic - Canyon": base_id + 60,
    "Fogbane Relic - Watchtower": base_id + 61,
    "Fogbane Relic - Haunted House": base_id + 62,
    "Fogbane Relic - Santiago House": base_id + 63,
    "Fogbane Relic - Port": base_id + 64,
    "Fogbane Relic - Doll Woods": base_id + 65,
    "Fogbane Relic - East House": base_id + 66,
    "Fogbane Relic - Rocket Grounds": base_id + 67,
    "Fogbane Relic - Workshop": base_id + 68,
    "Fogbane Relic - East Tower": base_id + 69,
    "Fogbane Relic - Lighthouse": base_id + 70,
    "Fogbane Relic - North Mine Outside": base_id + 71,
    "Fogbane Relic - Wood Bridge": base_id + 72,
    "Fogbane Relic - Museum": base_id + 73,
    "Fogbane Relic - Barbed Shelter": base_id + 74,
    "Fogbane Relic - West Beach": base_id + 75,
    "Fogbane Relic - Church": base_id + 76,
    "Fogbane Relic - West Cottage": base_id + 77,
    "Fogbane Relic - Trailer Cabin": base_id + 78,
    "Fogbane Relic - Towers": base_id + 79,
    "Fogbane Relic - North Beach": base_id + 80,
    "Fogbane Relic - Mob Camp": base_id + 81,
    "Fogbane Relic - Mine Elevator Exit": base_id + 82,
    "Fogbane Relic - Mountain Ruin Outside": base_id + 83,
    "Fogbane Relic - Temple": base_id + 84,
    "Fogbane Relic - Pickle Val": base_id + 85,
    "Fogbane Relic - Morse Bunker": base_id + 86
}

item_groups = {
    "Weapons": {
        "Bug Spray",
        "The Boomer",
        "Bob"
    },
    "Paint Can": {
        "Orange Paint Can",
        "Green Paint Can",
        "White Paint Can",
        "Pink Paint Can",
        "Grey Paint Can",
        "Blue Paint Can",
        "Black Paint Can",
        "Lime Paint Can",
        "Teal Paint Can",
        "Red Paint Can",
        "Purple Paint Can"
    },
    "Train Upgrade": {
        "Scraps",
        "30 Scraps Reward",
        "25 Scraps Reward",
        "35 Scraps Reward",
        "40 Scraps Reward",
        "Speed Unlock",
        "Damage Unlock",
        "Armor Unlock",
        "Speed Level",
        "Damage Level",
        "Armor Level"
    },
    "Mine Keys": {
        "South Mine Key",
        "North Mine Key",
        "Mountain Ruin Key"
    },
    "Building Keys": {
        "Barn Key",
        "Candice's Key",
        "Mob Camp Key",
        "Temple Key"
    },
    "Mission Items": {
        "Dead Fish",
        "Lockpicks",
        "Ancient Tablet",
        "Blue Box",
        "Page Drawing",
        "Journal",
        "Timed Dynamite",
        "Box of Rockets",
        "Breaker",
        "Broken Bob",
        "Employment Contracts",
        "Jar of Pickles",
        "Remote Explosive",
        "Remote Explosive x8"
    },
    "Eggs": {
        "Green Egg",
        "Blue Egg",
        "Red Egg"
    },
    "Fogbane Relics": {
        "Fogbane Relic Pack",
        "Fogbane Relic - Mine Shaft",
        "Fogbane Relic - Junkyard Area",
        "Fogbane Relic - Junkyard Shed",
        "Fogbane Relic - South House",
        "Fogbane Relic - Military Base",
        "Fogbane Relic - South Mine Outside",
        "Fogbane Relic - Middle Station",
        "Fogbane Relic - Canyon",
        "Fogbane Relic - Watchtower",
        "Fogbane Relic - Haunted House",
        "Fogbane Relic - Santiago House",
        "Fogbane Relic - Port",
        "Fogbane Relic - Doll Woods",
        "Fogbane Relic - East House",
        "Fogbane Relic - Rocket Grounds",
        "Fogbane Relic - Workshop",
        "Fogbane Relic - East Tower",
        "Fogbane Relic - Lighthouse",
        "Fogbane Relic - North Mine Outside",
        "Fogbane Relic - Wood Bridge",
        "Fogbane Relic - Museum",
        "Fogbane Relic - Barbed Shelter",
        "Fogbane Relic - West Beach",
        "Fogbane Relic - Church",
        "Fogbane Relic - West Cottage",
        "Fogbane Relic - Trailer Cabin",
        "Fogbane Relic - Towers",
        "Fogbane Relic - North Beach",
        "Fogbane Relic - Mob Camp",
        "Fogbane Relic - Mine Elevator Exit",
        "Fogbane Relic - Mountain Ruin Outside",
        "Fogbane Relic - Temple",
        "Fogbane Relic - Pickle Val",
        "Fogbane Relic - Morse Bunker"
    },
    "Track Switches": {
        "Track Switch Pack",
        "Track Switch - Barn or Tutorial",
        "Track Switch - Middle or Port",
        "Track Switch - Haunted or East",
        "Track Switch - North or Temple",
        "Track Switch - Caravan or Cultists",
        "Track Switch - Camp or Elevator",
        "Track Switch - Ruin or Temple"
    }
}


# All items excepted the duplications (no item amount)
unique_item_dict = {**optional_items, **useless_items, **progression_items}
