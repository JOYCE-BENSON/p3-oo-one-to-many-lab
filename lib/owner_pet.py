class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        
        # Validate pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Pet type must be one of {self.PET_TYPES}")
        self.pet_type = pet_type
        
        # Set owner if provided
        self.owner = owner
        
        # Add pet to all pets list
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        """Returns all pets owned by this owner"""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Adds a pet to this owner after validating it's a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added")
        pet.owner = self
    
    def get_sorted_pets(self):
        """Returns pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
    pass