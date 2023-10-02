# This Python file uses the following encoding: utf-8

from item import Item, ItemType, IModBit, ItemCapability, DamageType


class MBAxe(Item):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)
        # - - -
        self.set_type(ItemType.ONE_HANDED_WEAPON)
        # - - -
        self.add_capability(ItemCapability.HORSEBACK_ONEHANDED_OVERSWING_LEFT)
        self.add_capability(ItemCapability.HORSEBACK_ONEHANDED_OVERSWING_RIGHT)
        self.add_capability(ItemCapability.HORSEBACK_ONEHANDED_THRUST)
        # - - -
        self.add_capability(ItemCapability.ONEHANDED_OVERSWING)
        self.add_capability(ItemCapability.ONEHANDED_TRUST)
        self.add_capability(ItemCapability.ONEHANDED_PARRY_UP)
        self.add_capability(ItemCapability.ONEHANDED_PARRY_FORWARD)
        self.add_capability(ItemCapability.ONEHANDED_PARRY_LEFT)
        self.add_capability(ItemCapability.ONEHANDED_PARRY_RIGHT)
        # - - -
        self.add_capability(ItemCapability.CARRY_AXE_LEFT_HIP)
        # - - -
        self.add_modifier(IModBit.AXE)



    def set_speed(self, speed_rating : int):
        self.speed_rating = speed_rating


    def set_length(self, length : int):
        self.weapon_length = length


    def set_thrust_damage(self, damage : int, damage_type : DamageType):
        self.thrust_damage = (damage, damage_type.value)


    def set_swing_damage(self, damage : int, damage_type : DamageType):
        self.swing_damage = (damage, damage_type.value)

