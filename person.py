# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender

    # Define the introduce method
    def introduce(self):
        # Print the introduction message
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Dero", 20, "Male")

# Call the introduce method to display the person's information
person1.introduce()
