from dataclasses import dataclass
from Options import (
    StartInventoryPool, PerGameCommonOptions, DefaultOnToggle, Range, Toggle, DeathLink, Choice, Visibility
)


class TrackSwitches(Choice):
    """
    Randomize the track switches.

    **No:** Disabled.

    **Once:** When a switch is received, enable all the track switches.

    **All:** The 7 track switches are randomized.
    """
    display_name = "Track switches"
    option_no = 0
    option_once = 1
    option_all = 2
    default = 2
    visibility = Visibility.all


class CursedFogs(Choice):
    """
    Add non-interaction zones called 'Cursed Fogs' to several open regions.
    34 out of 43 regions will be cursed.
    You must obtain randomized 'Fogbane Relics' to clear the fogs.
    This option is designed to add more Spheres (it does not exist in the base game).

    **No:** Disabled.

    **Once:** When a Fogbane Relic is received, clear all the Cursed Fogs.

    **All:** One Fogbane Relic clears one Cursed Fog (34 relics for 34 regions).
    """
    display_name = "Cursed Fogs"
    option_no = 0
    option_once = 1
    option_all = 2
    default = 2
    visibility = Visibility.all


class SpeedBlueprintFragments(Choice):
    """
    Speed blueprint or fragments must be received to access the speed upgrade of the train.

    **No:** Disabled.

    **Blueprint:** The speed upgrade is locked until its blueprint is received (still needs scraps to upgrade).

    **Fragments:** The speed upgrade is disabled, it freely upgrades when a fragment is received (9 in total).
    """
    display_name = "Speed blueprint fragments"
    option_no = 0
    option_blueprints = 1
    option_fragments = 2
    default = 0
    visibility = Visibility.all


class DamageBlueprintFragments(Choice):
    """
    Damage blueprint or fragments must be received to access the damage upgrade of the train.

    **No:** Disabled.

    **Blueprint:** The damage upgrade is locked until its blueprint is received (still needs scraps to upgrade).

    **Fragments:** The damage upgrade is disabled, it freely upgrades when a fragment is received (9 in total).
    """
    display_name = "Damage blueprint fragments"
    option_no = 0
    option_blueprints = 1
    option_fragments = 2
    default = 0
    visibility = Visibility.all


class ArmorBlueprintFragments(Choice):
    """
    Armor blueprint or fragments must be received to access the armor upgrade of the train.

    **No:** Disabled.

    **Blueprint:** The armor upgrade is locked until its blueprint is received (still needs scraps to upgrade).

    **Fragments:** The armor upgrade is disabled, it freely upgrades when a fragment is received (9 in total).
    """
    display_name = "Armor blueprint fragments"
    option_no = 0
    option_blueprints = 1
    option_fragments = 2
    default = 0
    visibility = Visibility.all


@dataclass
class CCCharlesOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    track_switches: TrackSwitches
    cursed_fogs: CursedFogs
    speed_blueprint_fragments: SpeedBlueprintFragments
    damage_blueprint_fragments: DamageBlueprintFragments
    armor_blueprint_fragments: ArmorBlueprintFragments
    death_link: DeathLink
