
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase, digits as numbers

class Passmaker:
    

    def __init__(self, characterNumber, caracteresType, passwordsNumber):
        self.character_number =  characterNumber
        self.chacters_type = caracteresType
        self.password_number = passwordsNumber
        self._password_config = None

        self.caracters_all = lowercase + uppercase + numbers 

    
    def set_passwordsConfigation(self):
        self._password_config = {
            "passwords": self.password_number, 
            "characters": self.chacters_type,
            "size": self.character_number
            }
            
        return self._password_config
    

    
        

