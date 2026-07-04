from .Items import CCCharlesItem, unique_item_dict, item_groups
from .Locations import location_table
from .Options import CCCharlesOptions
from .Rules import set_rules
from .Regions import create_regions
from BaseClasses import Tutorial, ItemClassification
from worlds.AutoWorld import InvalidItemError, World, WebWorld
from typing import Any


class CCCharlesWeb(WebWorld):
    """
    Choo-Choo Charles is a horror game.
    A devil spider train from hell called Charles chases any person it finds on an island.
    The goal is to gather scraps to upgrade a train to fight Charles and travel by train to find 3 eggs
    to lead Charles to a brutal death and save the island.
    """

    theme = "stone"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setup Choo-Choo Charles for the Archipelago MultiWorld Randomizer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Yaranorgoth"]
    )

    setup_fr = Tutorial(
        "Guide d'Installation Multiworld",
        "Un guide pour mettre en place Choo-Choo Charles pour le Randomiseur Multiworld Archipelago",
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["Yaranorgoth"]
    )

    tutorials = [setup_en, setup_fr]

    game_info_languages = ["en", "fr"]
    rich_text_options_doc = True


class CCCharlesWorld(World):
    """ 
    An independent 3D horror game, taking place on an island.
    The main gameplay consists of traveling and fighting a monster on board a train.
    Upgrading the train requires leaving the train to gather resources with the threat of encountering the monster.
    """

    game = "Choo-Choo Charles"

    web = CCCharlesWeb()

    item_name_to_id = unique_item_dict
    location_name_to_id = location_table
    item_name_groups = item_groups

    # Options the player can set
    options_dataclass = CCCharlesOptions
    # Typing hints for all the options we defined
    options: CCCharlesOptions

    topology_present = False # Hide path to required location checks in spoiler

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.options, self.player)

    def create_item(self, name: str) -> CCCharlesItem:
        item_id = unique_item_dict[name]

        match name:
            case "Scraps":
                classification = ItemClassification.useful
            case "30 Scraps Reward":
                classification = ItemClassification.useful
            case "25 Scraps Reward":
                classification = ItemClassification.useful
            case "35 Scraps Reward":
                classification = ItemClassification.useful
            case "40 Scraps Reward":
                classification = ItemClassification.useful
            case "South Mine Key":
                classification = ItemClassification.progression
            case "North Mine Key":
                classification = ItemClassification.progression
            case "Mountain Ruin Key":
                classification = ItemClassification.progression
            case "Barn Key":
                classification = ItemClassification.progression
            case "Candice's Key":
                classification = ItemClassification.progression
            case "Dead Fish":
                classification = ItemClassification.progression
            case "Lockpicks":
                classification = ItemClassification.progression
            case "Ancient Tablet":
                classification = ItemClassification.progression
            case "Blue Box":
                classification = ItemClassification.progression
            case "Page Drawing":
                classification = ItemClassification.progression
            case "Journal":
                classification = ItemClassification.progression
            case "Timed Dynamite":
                classification = ItemClassification.progression
            case "Box of Rockets":
                classification = ItemClassification.progression
            case "Breaker":
                classification = ItemClassification.progression
            case "Broken Bob":
                classification = ItemClassification.progression
            case "Employment Contracts":
                classification = ItemClassification.progression
            case "Mob Camp Key":
                classification = ItemClassification.progression
            case "Jar of Pickles":
                classification = ItemClassification.progression
            case "Orange Paint Can":
                classification = ItemClassification.filler
            case "Green Paint Can":
                classification = ItemClassification.filler
            case "White Paint Can":
                classification = ItemClassification.filler
            case "Pink Paint Can":
                classification = ItemClassification.filler
            case "Grey Paint Can":
                classification = ItemClassification.filler
            case "Blue Paint Can":
                classification = ItemClassification.filler
            case "Black Paint Can":
                classification = ItemClassification.filler
            case "Lime Paint Can":
                classification = ItemClassification.filler
            case "Teal Paint Can":
                classification = ItemClassification.filler
            case "Red Paint Can":
                classification = ItemClassification.filler
            case "Purple Paint Can":
                classification = ItemClassification.filler
            case "The Boomer":
                classification = ItemClassification.useful
            case "Bob":
                classification = ItemClassification.useful
            case "Green Egg":
                classification = ItemClassification.progression
            case "Blue Egg":
                classification = ItemClassification.progression
            case "Red Egg":
                classification = ItemClassification.progression
            case "Remote Explosive":
                classification = ItemClassification.progression
            case "Remote Explosive x8":
                classification = ItemClassification.progression
            case "Temple Key":
                classification = ItemClassification.progression
            case "Bug Spray":
                classification = ItemClassification.progression
            case "Track Switch Pack":
                classification = ItemClassification.useful
            case "Track Switch - Barn or Tutorial":
                classification = ItemClassification.useful
            case "Track Switch - Middle or Port":
                classification = ItemClassification.useful
            case "Track Switch - Haunted or East":
                classification = ItemClassification.useful
            case "Track Switch - North or Temple":
                classification = ItemClassification.useful
            case "Track Switch - Caravan or Cultists":
                classification = ItemClassification.useful
            case "Track Switch - Camp or Elevator":
                classification = ItemClassification.useful
            case "Track Switch - Ruin or Temple":
                classification = ItemClassification.useful
            case "Fogbane Relic Pack":
                classification = ItemClassification.progression
            case "Fogbane Relic - Mine Shaft":
                classification = ItemClassification.progression
            case "Fogbane Relic - Junkyard Area":
                classification = ItemClassification.progression
            case "Fogbane Relic - Junkyard Shed":
                classification = ItemClassification.progression
            case "Fogbane Relic - South House":
                classification = ItemClassification.progression
            case "Fogbane Relic - Military Base":
                classification = ItemClassification.progression
            case "Fogbane Relic - South Mine Outside":
                classification = ItemClassification.progression
            case "Fogbane Relic - Middle Station":
                classification = ItemClassification.progression
            case "Fogbane Relic - Canyon":
                classification = ItemClassification.progression
            case "Fogbane Relic - Watchtower":
                classification = ItemClassification.progression
            case "Fogbane Relic - Haunted House":
                classification = ItemClassification.progression
            case "Fogbane Relic - Santiago House":
                classification = ItemClassification.progression
            case "Fogbane Relic - Port":
                classification = ItemClassification.progression
            case "Fogbane Relic - Doll Woods":
                classification = ItemClassification.progression
            case "Fogbane Relic - East House":
                classification = ItemClassification.progression
            case "Fogbane Relic - Rocket Grounds":
                classification = ItemClassification.progression
            case "Fogbane Relic - Workshop":
                classification = ItemClassification.progression
            case "Fogbane Relic - East Tower":
                classification = ItemClassification.progression
            case "Fogbane Relic - Lighthouse":
                classification = ItemClassification.progression
            case "Fogbane Relic - North Mine Outside":
                classification = ItemClassification.progression
            case "Fogbane Relic - Wood Bridge":
                classification = ItemClassification.progression
            case "Fogbane Relic - Museum":
                classification = ItemClassification.progression
            case "Fogbane Relic - Barbed Shelter":
                classification = ItemClassification.progression
            case "Fogbane Relic - West Beach":
                classification = ItemClassification.progression
            case "Fogbane Relic - Church":
                classification = ItemClassification.progression
            case "Fogbane Relic - West Cottage":
                classification = ItemClassification.progression
            case "Fogbane Relic - Trailer Cabin":
                classification = ItemClassification.progression
            case "Fogbane Relic - Towers":
                classification = ItemClassification.progression
            case "Fogbane Relic - North Beach":
                classification = ItemClassification.progression
            case "Fogbane Relic - Mob Camp":
                classification = ItemClassification.progression
            case "Fogbane Relic - Mine Elevator Exit":
                classification = ItemClassification.progression
            case "Fogbane Relic - Mountain Ruin Outside":
                classification = ItemClassification.progression
            case "Fogbane Relic - Temple":
                classification = ItemClassification.progression
            case "Fogbane Relic - Pickle Val":
                classification = ItemClassification.progression
            case "Fogbane Relic - Morse Bunker":
                classification = ItemClassification.progression
            case "Speed blueprint":
                classification = ItemClassification.useful
            case "Damage blueprint":
                classification = ItemClassification.useful
            case "Armor blueprint":
                classification = ItemClassification.useful
            case "Speed fragment":
                classification = ItemClassification.useful
            case "Damage fragment":
                classification = ItemClassification.useful
            case "Armor fragment":
                classification = ItemClassification.useful
            case _: # Should not occur
                raise InvalidItemError("Unexpected case met: classification cannot be set for unknown item \"" + name + "\"")

        return CCCharlesItem(name, classification, item_id, self.player)

    def create_items(self) -> None:
        # Main rule: the number of items and locations must be equal (692 locations)
        number_of_scraps = 638 # max: 637 + 1 reward from Ronny

        # Add items to full_item_list based on Player Options
        full_item_list = []
        if self.options.track_switches == "once":
            full_item_list += ["Track Switch Pack"] * 1
            number_of_scraps -= 1
        elif self.options.track_switches == "all":
            full_item_list += ["Track Switch - Barn or Tutorial"] * 1
            full_item_list += ["Track Switch - Middle or Port"] * 1
            full_item_list += ["Track Switch - Haunted or East"] * 1
            full_item_list += ["Track Switch - North or Temple"] * 1
            full_item_list += ["Track Switch - Caravan or Cultists"] * 1
            full_item_list += ["Track Switch - Camp or Elevator"] * 1
            full_item_list += ["Track Switch - Ruin or Temple"] * 1
            number_of_scraps -= 7
        if self.options.cursed_fogs == "once":
            full_item_list += ["Fogbane Relic Pack"] * 1
            number_of_scraps -= 1
        elif self.options.cursed_fogs == "all":
            full_item_list += ["Fogbane Relic - Mine Shaft"] * 1
            full_item_list += ["Fogbane Relic - Junkyard Area"] * 1
            full_item_list += ["Fogbane Relic - Junkyard Shed"] * 1
            full_item_list += ["Fogbane Relic - South House"] * 1
            full_item_list += ["Fogbane Relic - Military Base"] * 1
            full_item_list += ["Fogbane Relic - South Mine Outside"] * 1
            full_item_list += ["Fogbane Relic - Middle Station"] * 1
            full_item_list += ["Fogbane Relic - Canyon"] * 1
            full_item_list += ["Fogbane Relic - Watchtower"] * 1
            full_item_list += ["Fogbane Relic - Haunted House"] * 1
            full_item_list += ["Fogbane Relic - Santiago House"] * 1
            full_item_list += ["Fogbane Relic - Port"] * 1
            full_item_list += ["Fogbane Relic - Doll Woods"] * 1
            full_item_list += ["Fogbane Relic - East House"] * 1
            full_item_list += ["Fogbane Relic - Rocket Grounds"] * 1
            full_item_list += ["Fogbane Relic - Workshop"] * 1
            full_item_list += ["Fogbane Relic - East Tower"] * 1
            full_item_list += ["Fogbane Relic - Lighthouse"] * 1
            full_item_list += ["Fogbane Relic - North Mine Outside"] * 1
            full_item_list += ["Fogbane Relic - Wood Bridge"] * 1
            full_item_list += ["Fogbane Relic - Museum"] * 1
            full_item_list += ["Fogbane Relic - Barbed Shelter"] * 1
            full_item_list += ["Fogbane Relic - West Beach"] * 1
            full_item_list += ["Fogbane Relic - Church"] * 1
            full_item_list += ["Fogbane Relic - West Cottage"] * 1
            full_item_list += ["Fogbane Relic - Trailer Cabin"] * 1
            full_item_list += ["Fogbane Relic - Towers"] * 1
            full_item_list += ["Fogbane Relic - North Beach"] * 1
            full_item_list += ["Fogbane Relic - Mob Camp"] * 1
            full_item_list += ["Fogbane Relic - Mine Elevator Exit"] * 1
            full_item_list += ["Fogbane Relic - Mountain Ruin Outside"] * 1
            full_item_list += ["Fogbane Relic - Temple"] * 1
            full_item_list += ["Fogbane Relic - Pickle Val"] * 1
            full_item_list += ["Fogbane Relic - Morse Bunker"] * 1
            number_of_scraps -= 34
        if self.options.speed_blueprint_fragments == "blueprints":
            full_item_list += ["Speed blueprint"] * 1
            number_of_scraps -= 1
        elif self.options.speed_blueprint_fragments == "fragments":
            full_item_list += ["Speed fragments"] * 9
            number_of_scraps -= 9
        if self.options.damage_blueprint_fragments == "blueprints":
            full_item_list += ["Damage blueprint"] * 1
            number_of_scraps -= 1
        elif self.options.damage_blueprint_fragments == "fragments":
            full_item_list += ["Damage fragments"] * 9
            number_of_scraps -= 9
        if self.options.armor_blueprint_fragments == "blueprints":
            full_item_list += ["Armor blueprint"] * 1
            number_of_scraps -= 1
        elif self.options.armor_blueprint_fragments == "fragments":
            full_item_list += ["Armor fragments"] * 9
            number_of_scraps -= 9

        full_item_list += ["Scraps"] * number_of_scraps
        full_item_list += ["30 Scraps Reward"] * 3
        full_item_list += ["25 Scraps Reward"] * 1
        full_item_list += ["35 Scraps Reward"] * 2
        full_item_list += ["40 Scraps Reward"] * 1
        full_item_list += ["South Mine Key"] * 1
        full_item_list += ["North Mine Key"] * 1
        full_item_list += ["Mountain Ruin Key"] * 1
        full_item_list += ["Barn Key"] * 1
        full_item_list += ["Candice's Key"] * 1
        full_item_list += ["Dead Fish"] * 1
        full_item_list += ["Lockpicks"] * 1
        full_item_list += ["Ancient Tablet"] * 1
        full_item_list += ["Blue Box"] * 1
        full_item_list += ["Page Drawing"] * 8
        full_item_list += ["Journal"] * 1
        full_item_list += ["Timed Dynamite"] * 1
        full_item_list += ["Box of Rockets"] * 1
        full_item_list += ["Breaker"] * 4
        full_item_list += ["Broken Bob"] * 1
        full_item_list += ["Employment Contracts"] * 1
        full_item_list += ["Mob Camp Key"] * 1
        full_item_list += ["Jar of Pickles"] * 1
        full_item_list += ["Orange Paint Can"] * 1
        full_item_list += ["Green Paint Can"] * 1
        full_item_list += ["White Paint Can"] * 1
        full_item_list += ["Pink Paint Can"] * 1
        full_item_list += ["Grey Paint Can"] * 1
        full_item_list += ["Blue Paint Can"] * 1
        full_item_list += ["Black Paint Can"] * 1
        full_item_list += ["Lime Paint Can"] * 1
        full_item_list += ["Teal Paint Can"] * 1
        full_item_list += ["Red Paint Can"] * 1
        full_item_list += ["Purple Paint Can"] * 1
        full_item_list += ["The Boomer"] * 1
        full_item_list += ["Bob"] * 1
        full_item_list += ["Green Egg"] * 1
        full_item_list += ["Blue Egg"] * 1
        full_item_list += ["Red Egg"] * 1
        full_item_list += ["Remote Explosive x8"] * 1
        full_item_list += ["Temple Key"] * 1
        full_item_list += ["Bug Spray"] * 1

        self.multiworld.itempool += [self.create_item(item) for item in full_item_list]

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.options, self.player)

    def get_filler_item_name(self) -> str:
        return "Scraps"

    def fill_slot_data(self) -> dict[str, Any]:
        slot_data = {
            "world_version": self.world_version.as_simple_string(), # See archipelago.json: check mod<->apworld compliance
            "TrackSwitches": self.options.track_switches.value,
            "CursedFogs": self.options.cursed_fogs.value,
            "SpeedBlueprintFragments": self.options.speed_blueprint_fragments.value,
            "DamageBlueprintFragments": self.options.damage_blueprint_fragments.value,
            "ArmorBlueprintFragments": self.options.armor_blueprint_fragments.value,
            "DeathLink": self.options.death_link.value
        }
        return slot_data
