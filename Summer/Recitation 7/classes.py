class Person:
    
    # Class Attribute
    species = 'Homo sapien'
    
    # Initializer / Instance Attributes
    def __init__(self, name, age, emotion, glasses):
        self.name = name
        self.age = age
        self.emotion = emotion
        self.glasses = glasses
        
    # instance method
    def description(self):
        print("{} is {} and is {}.".format(self.name, self.age, self.emotion))
        
    def set_emotion(self, new_emotion):
        self.emotion = new_emotion
    def get_emotion(self):
        return self.emotion
    
    def set_age(self, new_age):
        if new_age < 0 or new_age > 500:
            print('not a valid age!')
        else:
            self.age = new_age
