
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase, digits as numbers
import random 



class Passmaker:
    def __init__(self, characterNumber, passwordsNumber, charactersType):
        self.character_number =  characterNumber
        self.chacters_type = charactersType
        self.password_number = passwordsNumber

        self.config = None

        self.characters_all = lowercase + uppercase + numbers + "!#$%&"
        self.password_list = []




    def set_passConfig(self):
        self.config = {
            "passwords": self.password_number, 
            "characters": self.chacters_type,
            "size": self.character_number
            }
        return self.config




    def construct(self):
        for _ in range(0, self.config['passwords']):
            list_characters = []

            for _ in range(0, self.config['size']):
                list_characters.append(random.choice(self.characters_all))
            password = "".join(list_characters)

            self.password_list.append(password)
            
        return self.password_list

    
        

