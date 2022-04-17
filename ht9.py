from random import randint 
 

class Gun: 
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
        return self.barrel_length * dice > 100 


class Ammo: 
    def __init__(self, gun: Gun, ammo_type) -> None: 
        self.gun = gun
        self.ammo_type = ammo_type 
       
    def get_damage(self): 
        """Returns damage made by the ammo being ammo caliber multiplied with 3. 

        Incoming values - ammo caliber (depending on the gun)  
        and type of ammo (can be explosive, cumulative or sub-caliber)""" 
        return self.gun.caliber * 3 

    def get_penetration(self): 
        """Shows gun's possibility to break through the armor 
        by returning ammo_caliber""" 
        return self.gun.caliber 


class HECartridge(Ammo): 
    def __init__(self, gun: Gun) -> None:
        super().__init__(gun, 'фугасный') 

    
class HEATCartridge(Ammo): 
    def __init__(self, gun: Gun) -> None:
        super().__init__(gun, 'кумулятивный') 

    def get_damage(self):  
        """Returns damage made by the HEATCartridge""" 
        return super().get_damage() * 0.6 
 
 
class APCartridge(Ammo): 
    def __init__(self, gun: Gun) -> None:
        super().__init__(gun, 'подкалиберный') 
 
    def get_damage(self):  
        """Returns damage made by the APCartridge""" 
        return super().get_damage() * 0.3 


class Armour(): 
    def __init__(self, thickness, armour_type) -> None: 
        self.thickness = thickness 
        self.armour_type = armour_type 

    def is_penetrated(self, ammo: Ammo) -> bool:
        return ammo.get_penetration() > self.thickness


class HArmour(Armour): 
    def __init__(self, thickness): 
        super().__init__(self, thickness, 'гомогенная') 

    def is_penetrated(self, ammo: Ammo): 
        if ammo_type == 'фугасный': 
            return ammo.get_penetration > self.thickness * 1.2 
        elif ammo_type == 'кумулятивный': 
            return ammo.get_penetration > self.thickness * 1 
        elif ammo_type == 'подкалиберный': 
            return ammo.get_penetration > self.thickness * 0.7 
        else: 
            return False 

class SArmour(Armour): 
    def __init__(self, thickness): 
        super().__init__(self, thickness, 'стальная') 

    def is_penetrated(self, ammo: Ammo): 
        if ammo_type == 'фугасный': 
            return ammo.get_penetration > self.thickness * 1.5 
        elif ammo_type == 'кумулятивный': 
            return ammo.get_penetration > self.thickness * 1.3 
        elif ammo_type == 'подкалиберный': 
            return ammo.get_penetration > self.thickness * 0.9 
        else: 
            return False 


class СArmour(Armour): 
    def __init__(self, thickness): 
        super().__init__(self, thickness, 'керамическая') 

    def is_penetrated(self, ammo: Ammo): 
        if ammo_type == 'фугасный': 
            return ammo.get_penetration > self.thickness * 1.1 
        elif ammo_type == 'кумулятивный': 
            return ammo.get_penetration > self.thickness * 0.9 
        elif ammo_type == 'подкалиберный': 
            return ammo.get_penetration > self.thickness * 0.7 
        else: 
            return False

#g1 = Gun(15, 25) 
#a1 = Ammo(15, 25, 'explosive') 


if __name__ == '__main__': 
    print(a1.type) 