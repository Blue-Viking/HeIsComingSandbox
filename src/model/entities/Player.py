from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.data import EquipmentInstance
    from model.effects import StatusEffect

class Player:
    def __init__(self, name: str, hp: int, attack: int, speed: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.equipment: list = []  # EquipmentInstance
        self.status_effects: list = []  # StatusEffect

    @property
    def alive(self) -> bool:
        return self.hp > 0