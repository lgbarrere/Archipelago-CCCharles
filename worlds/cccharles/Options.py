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


class SpeedUpgrade(Choice):
    """
    The speed upgrade of the train must be unlocked or speed levels must be received.

    **No:** Disabled.

    **Unlock:** The speed upgrade is locked until it is received (still needs scraps to upgrade).

    **Levels:** The speed upgrade is disabled, it freely upgrades when a speed level is received (9 in total).
    """
    display_name = "Speed Upgrade"
    option_no = 0
    option_unlock = 1
    option_levels = 2
    default = 0
    visibility = Visibility.all


class DamageUpgrade(Choice):
    """
    The damage upgrade of the train must be unlocked or damage levels must be received.

    **No:** Disabled.

    **Unlock:** The damage upgrade is locked until it is received (still needs scraps to upgrade).

    **Levels:** The damage upgrade is disabled, it freely upgrades when a damage level is received (9 in total).
    """
    display_name = "Damage Upgrade"
    option_no = 0
    option_unlock = 1
    option_levels = 2
    default = 0
    visibility = Visibility.all


class ArmorUpgrade(Choice):
    """
    The armor upgrade of the train must be unlocked or armor levels must be received.

    **No:** Disabled.

    **Unlock:** The armor upgrade is locked until it is received (still needs scraps to upgrade).

    **Levels:** The armor upgrade is disabled, it freely upgrades when an armor level is received (9 in total).
    """
    display_name = "Armor Upgrade"
    option_no = 0
    option_unlock = 1
    option_levels = 2
    default = 0
    visibility = Visibility.all


@dataclass
class CCCharlesOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    track_switches: TrackSwitches
    cursed_fogs: CursedFogs
    speed_upgrade: SpeedUpgrade
    damage_upgrade: DamageUpgrade
    armor_upgrade: ArmorUpgrade
    death_link: DeathLink
