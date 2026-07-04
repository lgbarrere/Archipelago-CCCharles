from BaseClasses import MultiWorld
from ..generic.Rules import set_rule
from .Options import CCCharlesOptions

# Go mode: Green Egg + Blue Egg + Red Egg + Temple Key + Bug Spray (+ Remote Explosive x8 but the base game ignores it)

def set_rules(multiworld: MultiWorld, options: CCCharlesOptions, player: int) -> None:
    # Tony Tiddle
    set_rule(multiworld.get_entrance("Barn Door", player),
        lambda state: state.has("Barn Key", player))

    # Candice
    set_rule(multiworld.get_entrance("Tutorial House Door", player),
        lambda state: state.has("Candice's Key", player))

    # Lizbeth Murkwater
    set_rule(multiworld.get_location("Swamp Lizbeth Murkwater Mission End", player),
        lambda state: state.has("Dead Fish", player))

    # Daryl
    set_rule(multiworld.get_location("Junkyard Area Chest Ancient Tablet", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Junkyard Area Daryl Mission End", player),
        lambda state: state.has("Ancient Tablet", player))

    # South House
    set_rule(multiworld.get_location("South House Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("South House Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("South House Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("South House Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("South House Chest Scraps - 5", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("South House Chest Scraps - 6", player),
        lambda state: state.has("Lockpicks", player))

    # South Mine
    set_rule(multiworld.get_entrance("South Mine Gate", player),
        lambda state: state.has("South Mine Key", player))

    set_rule(multiworld.get_location("South Mine Inside Green Paint Can", player),
        lambda state: state.has("Lockpicks", player))

    # Theodore
    set_rule(multiworld.get_location("Middle Station Theodore Mission End", player),
        lambda state: state.has("Blue Box", player))

    # Watchtower
    set_rule(multiworld.get_location("Watchtower Pink Paint Can", player),
        lambda state: state.has("Lockpicks", player))

    # Sasha
    set_rule(multiworld.get_location("Haunted House Sasha Mission End", player),
        lambda state: state.has("Page Drawing", player, 8))

    # Santiago
    set_rule(multiworld.get_location("Port Santiago Mission End", player),
        lambda state: state.has("Journal", player))

    # Trench House
    set_rule(multiworld.get_location("Trench House Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Trench House Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Trench House Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Trench House Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Trench House Chest Scraps - 5", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Trench House Chest Scraps - 6", player),
        lambda state: state.has("Lockpicks", player))

    # East House
    set_rule(multiworld.get_location("East House Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("East House Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("East House Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("East House Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("East House Chest Scraps - 5", player),
        lambda state: state.has("Lockpicks", player))

    # Rocket Bunker
    set_rule(multiworld.get_entrance("Stuck Bunker Door", player),
        lambda state: state.has("Timed Dynamite", player))

    # John Smith
    set_rule(multiworld.get_location("Workshop John Smith Mission End", player),
        lambda state: state.has("Box of Rockets", player))

    # Claire
    set_rule(multiworld.get_location("Lighthouse Claire Mission End", player),
        lambda state: state.has("Breaker", player, 4))

    # North Mine
    set_rule(multiworld.get_entrance("North Mine Gate", player),
        lambda state: state.has("North Mine Key", player))

    set_rule(multiworld.get_location("North Mine Inside Blue Paint Can", player),
        lambda state: state.has("Lockpicks", player))

    # Paul
    set_rule(multiworld.get_location("Museum Paul Mission End", player),
        lambda state: state.has("Remote Explosive x8", player))
        # lambda state: state.has("Remote Explosive", player, 8)) # TODO: Add an option to split remote explosives

    # West Beach
    set_rule(multiworld.get_location("West Beach Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("West Beach Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("West Beach Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("West Beach Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("West Beach Chest Scraps - 5", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("West Beach Chest Scraps - 6", player),
        lambda state: state.has("Lockpicks", player))

    # Caravan
    set_rule(multiworld.get_location("Caravan Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Caravan Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Caravan Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Caravan Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Caravan Chest Scraps - 5", player),
        lambda state: state.has("Lockpicks", player))

    # Ronny
    set_rule(multiworld.get_location("Towers Ronny Mission End", player),
        lambda state: state.has("Employment Contracts", player))

    # North Beach
    set_rule(multiworld.get_location("North Beach Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("North Beach Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("North Beach Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("North Beach Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))

    # Mine Shaft
    set_rule(multiworld.get_location("Mine Shaft Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Mine Shaft Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Mine Shaft Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Mine Shaft Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Mine Shaft Chest Scraps - 5", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Mine Shaft Chest Scraps - 6", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Mine Shaft Chest Scraps - 7", player),
        lambda state: state.has("Lockpicks", player))

    # Mob Camp
    set_rule(multiworld.get_entrance("Mob Camp Locked Door", player),
        lambda state: state.has("Mob Camp Key", player))

    set_rule(multiworld.get_location("Mob Camp Locked Room Stolen Bob", player),
        lambda state: state.has("Broken Bob", player))

    # Mountain Ruin
    set_rule(multiworld.get_entrance("Mountain Ruin Gate", player),
        lambda state: state.has("Mountain Ruin Key", player))

    set_rule(multiworld.get_location("Mountain Ruin Inside Red Paint Can", player),
        lambda state: state.has("Lockpicks", player))

    # Temple
    set_rule(multiworld.get_location("Temple Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Temple Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Temple Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))

    # Pickle Lady
    set_rule(multiworld.get_location("Pickle Val Jar of Pickles", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Pickle Val Pickle Lady Mission End", player),
        lambda state: state.has("Jar of Pickles", player))

    # Morse Bunker
    set_rule(multiworld.get_location("Morse Bunker Chest Scraps - 1", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Morse Bunker Chest Scraps - 2", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Morse Bunker Chest Scraps - 3", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Morse Bunker Chest Scraps - 4", player),
        lambda state: state.has("Lockpicks", player))
    set_rule(multiworld.get_location("Morse Bunker Chest Scraps - 5", player),
        lambda state: state.has("Lockpicks", player))

    # The Cursed Fogs (option)
    fogbane_relic_pack = "Fogbane Relic Pack"
    if options.cursed_fogs != "no":
        set_rule(multiworld.get_entrance("Mine Shaft Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Mine Shaft"), player))
        set_rule(multiworld.get_entrance("Junkyard Area Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Junkyard Area"), player))
        set_rule(multiworld.get_entrance("Junkyard Shed Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Junkyard Shed"), player))
        set_rule(multiworld.get_entrance("South House Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - South House"), player))
        set_rule(multiworld.get_entrance("Military Base Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Military Base"), player))
        set_rule(multiworld.get_entrance("South Mine Outside Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - South Mine Outside"), player))
        set_rule(multiworld.get_entrance("Middle Station Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Middle Station"), player))
        set_rule(multiworld.get_entrance("Canyon Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Canyon"), player))
        set_rule(multiworld.get_entrance("Watchtower Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Watchtower"), player))
        set_rule(multiworld.get_entrance("Haunted House Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Haunted House"), player))
        set_rule(multiworld.get_entrance("Santiago House Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Santiago House"), player))
        set_rule(multiworld.get_entrance("Port Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Port"), player))
        set_rule(multiworld.get_entrance("Doll Woods Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Doll Woods"), player))
        set_rule(multiworld.get_entrance("East House Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - East House"), player))
        set_rule(multiworld.get_entrance("Rocket Grounds Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Rocket Grounds"), player))
        set_rule(multiworld.get_entrance("Workshop Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Workshop"), player))
        set_rule(multiworld.get_entrance("East Tower Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - East Tower"), player))
        set_rule(multiworld.get_entrance("Lighthouse Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Lighthouse"), player))
        set_rule(multiworld.get_entrance("North Mine Outside Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - North Mine Outside"), player))
        set_rule(multiworld.get_entrance("Wood Bridge Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Wood Bridge"), player))
        set_rule(multiworld.get_entrance("Museum Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Museum"), player))
        set_rule(multiworld.get_entrance("Barbed Shelter Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Barbed Shelter"), player))
        set_rule(multiworld.get_entrance("West Beach Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - West Beach"), player))
        set_rule(multiworld.get_entrance("Church Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Church"), player))
        set_rule(multiworld.get_entrance("West Cottage Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - West Cottage"), player))
        set_rule(multiworld.get_entrance("Trailer Cabin Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Trailer Cabin"), player))
        set_rule(multiworld.get_entrance("Towers Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Towers"), player))
        set_rule(multiworld.get_entrance("North Beach Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - North Beach"), player))
        set_rule(multiworld.get_entrance("Mob Camp Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Mob Camp"), player))
        set_rule(multiworld.get_entrance("Mine Elevator Exit Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Mine Elevator Exit"), player))
        set_rule(multiworld.get_entrance("Mountain Ruin Outside Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Mountain Ruin Outside"), player))
        set_rule(multiworld.get_entrance("Temple Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Temple"), player))
        set_rule(multiworld.get_entrance("Pickle Val Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Pickle Val"), player))
        set_rule(multiworld.get_entrance("Morse Bunker Fogless", player),
            lambda state: state.has_any((fogbane_relic_pack, "Fogbane Relic - Morse Bunker"), player))

    # Add rules to reach the "Go mode"
    required_items = ["Temple Key", "Green Egg", "Blue Egg", "Red Egg"]
    if options.cursed_fogs == "once":
        required_items.append(fogbane_relic_pack)
    elif options.cursed_fogs == "all":
        required_items.append("Fogbane Relic - Temple") 

    set_rule(multiworld.get_location("Final Boss", player),
        lambda state: state.has_all(required_items, player))
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
