class Person:
    def __init__(self, speak, walk, get_name, get_age):
        self.speak = speak
        self.walk = walk
        self.get_name = get_name
        self.get_age = get_age

    def sound(self):
        return f"the boy can {self.speak} fluently in Asante Twi"
    
    def motion(self):
        return "i can {self.walk} faster than Usain Bolt"
    
    def description(self):
        return f"my name is {self.get_name} and i am {self.get_age}"
    
rock = Person("talk", "run", "ansah", "14")
k = rock.sound
print(k)

