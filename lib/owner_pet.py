class Owner:
    def _init_(self, name):
        self.name = name
        # Initialize an empty list to store the owner's pets
        self._pets = []

    def pets(self):
        """
        Returns a full list of the owner's pets.
        """
        return self._pets

    def add_pet(self, pet):
        """
        Checks that the pet is of type Pet and adds the owner to the pet.
        """
        if not isinstance(pet, Pet):
            raise Exception("The provided pet must be an instance of the Pet class.")
        
        # Set the owner of the pet
        pet.owner = self

        # Add the pet to the owner's list of pets if it's not already there
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        """
        Returns a sorted list of pets by their names.
        """
        # Sort pets by their names
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def _init_(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: '{pet_type}'. Allowed types are: {', '.join(Pet.PET_TYPES)}")

        self.name = name
        self.pet_type = pet_type
        
        # Validate owner type if provided
        if owner and not isinstance(owner, Owner):
            raise Exception("The provided owner must be an instance of the Owner class.")
        
        self.owner = owner  # Optional owner attribute

        # If the owner is provided, add the pet to the owner's list of pets
        if owner:
            owner.add_pet(self)

        # Append the new instance to the class variable 'all'
        Pet.all.append(self)

    def display_pet(self):
        if self.owner:
            print(f"Pet Name: {self.name}, Type: {self.pet_type}, Owner: {self.owner.name}")
        else:
            print(f"Pet Name: {self.name}, Type: {self.pet_type}, Owner: None")

    @classmethod
    def display_all_pets(cls):
        for pet in cls.all:
            pet.display_pet()