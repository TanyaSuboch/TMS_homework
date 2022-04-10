from random import randint
from unittest import result

class Gun():

    def __init__(self, caliber, barrel_length) -> None:

        self.caliber = caliber
        self.barrel_length = barrel_length

    
    def is_on_target(self):
        """Returns the result of gun's attack - either reached the target or not.

        Result 'True' is printed once the meaning of 
        barrel length * dice is more than 100.

        Dice is a random integer values from 1 to 6.
        """
        dice = randint(1, 6)
        print(dice)
        result = self.barrel_length*dice
        if result > 100:
            return True
        else:
            return False


class Ammo():

    def __init__(self, caliber, barrel_length, type) -> None:
        self.caliber = caliber
        self.barrel_length = barrel_length
        self.type = type
        type = ['explosive', 'cumulative', 'sub-caliber']
        self.gun = Gun(self.caliber, self.barrel_length)
       
    def get_damage(self):
        """Returns damage made by the ammo being ammo caliber multiplied with 3.
 
        Incoming values - ammo caliber (depending on the gun) 
        and type of ammo (can be explosive, cumulative or sub-caliber)"""
        return (self.caliber * 3)
        
    def get_penetration(self):
        """Shows gun's possibility to break through the armor
        by returning ammo_caliber"""
        return self.caliber

class HECartridge(Ammo):

    def __init__(self, caliber, barrel_length, type = 'explosive'):
        super().__init__(self, caliber, barrel_length, type)
        
    def get_damage(self): 
        """Returns damage made by the HECartridge"""
        return super().get_damage()


class HEATCartridge(Ammo):
    
    def __init__(self, caliber, barrel_length, type = 'cumulative'):
        super().__init__(self, caliber, barrel_length, type)

    def get_damage(self): 
        """Returns damage made by the HEATCartridge"""
        return (super().get_damage() * 0.6)

class APCartridge(Ammo):
    
    def __init__(self, caliber, barrel_length, type = 'sub-caliber'):
        super().__init__(self, caliber, barrel_length, type)

    def get_damage(self): 
        """Returns damage made by the APCartridge"""
        return (super().get_damage() * 0.3)

class Armour():

    def __init__(self, thickness, type) -> None:
        self.thickness = thickness
        self.type = type
    
    def is_penetrated(self, ammo):
        self.ammo = ammo
        ammo = Ammo()
        return True if ammo.get_penetration > self.thickness else False

class HArmour(Armour):

    def __init__(self, thickness, type = 'homogenic'):
        Armour.__init__(self, thickness, type)

    def is_penetrated(self, ammo):
        self.ammo = ammo
        ammo = Ammo()
        if ammo.type == 'explosive':
            return ammo.get_penetration > self.thickness * 1.2
        elif ammo.type == 'cumulative':
            return ammo.get_penetration > self.thickness * 1
        elif ammo.type == 'sub-caliber':
            return ammo.get_penetration > self.thickness * 0.7
        else: False

#g1 = Gun(15, 25)
#a1 = Ammo(15, 25, 'explosive')

if __name__ == '__main__':
    print(a1.type)