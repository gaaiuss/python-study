"""
This module is meant to save a class data (attributes) into a json file.
"""

import json


class Hunter:
    def __init__(
        self,
        name: str,
        age: int,
        weapon_name: str,
        village_name: str,
        *,
        begginer: bool,
    ) -> None:
        self.name = name
        self.age = age
        self.weapon_name = weapon_name
        self.village_name = village_name
        self.begginer = begginer


hunter_amir = Hunter("Amir", 22, "Sword and Shield", "Kokoto Village", begginer=False)
hunter_yoruichi = Hunter(
    "Yoruichi", 26, "Hammer / Dual Blades", "Poke Village", begginer=False
)

hunter_data_list = vars(hunter_amir), hunter_yoruichi.__dict__

save_data_local = "savedata.json"

if __name__ == "__main__":
    with open(save_data_local, "w") as file:
        json.dump(hunter_data_list, file)
