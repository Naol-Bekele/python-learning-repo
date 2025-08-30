"""
Object-Oriented Programming utilities and examples.
"""

from collections import namedtuple
import math


class Dog:
    """
    A class representing a Dog with basic attributes and behaviors.

    Attributes:
        species (str): The species of the dog (class attribute)
        name (str): The name of the dog (instance attribute)
        age (int): The age of the dog in years (instance attribute)
    """

    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        """
        Initialize a new Dog instance.

        Args:
            name (str): The name of the dog
            age (int): The age of the dog in years
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        Return a string representation of the Dog.

        Returns:
            str: String representation
        """
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        """
        Make the dog speak.

        Args:
            sound (str): The sound the dog makes

        Returns:
            str: Formatted string with the dog's speech
        """
        return f"{self.name} says {sound}"


class JackRussellTerrier(Dog):
    """A specific breed of dog that inherits from Dog."""

    def speak(self, sound="Arf"):
        """
        Make the Jack Russell Terrier speak with a default sound.

        Args:
            sound (str, optional): The sound the dog makes. Defaults to "Arf".

        Returns:
            str: Formatted string with the dog's speech
        """
        return super().speak(sound)


class Dachshund(Dog):
    """A specific breed of dog that inherits from Dog."""

    pass


class Bulldog(Dog):
    """A specific breed of dog that inherits from Dog."""

    pass


class Rectangle:
    """
    A class representing a Rectangle.

    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """

    def __init__(self, length, width):
        """
        Initialize a new Rectangle instance.

        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle
        """
        return self.length * self.width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle
        """
        return 2 * (self.length + self.width)

    def is_square(self):
        """
        Check if the rectangle is a square.

        Returns:
            bool: True if length equals width, False otherwise
        """
        return self.length == self.width


class Square(Rectangle):
    """
    A class representing a Square, which inherits from Rectangle.

    Attributes:
        side_length (float): The length of each side of the square
    """

    def __init__(self, side_length):
        """
        Initialize a new Square instance.

        Args:
            side_length (float): The length of each side of the square
        """
        super().__init__(side_length, side_length)
        self.side_length = side_length


class Animal:
    """
    A base class representing an Animal.

    Attributes:
        name (str): The name of the animal
        age (int): The age of the animal in years
    """

    def __init__(self, name, age):
        """
        Initialize a new Animal instance.

        Args:
            name (str): The name of the animal
            age (int): The age of the animal in years
        """
        self.name = name
        self.age = age

    def speak(self, sound):
        """
        Make the animal speak.

        Args:
            sound (str): The sound the animal makes

        Returns:
            str: Formatted string with the animal's speech
        """
        return f"{self.name} says {sound}"

    def eat(self, food):
        """
        Make the animal eat.

        Args:
            food (str): The food the animal eats

        Returns:
            str: Formatted string with the animal's eating action
        """
        return f"{self.name} is eating {food}"

    def sleep(self):
        """
        Make the animal sleep.

        Returns:
            str: Formatted string with the animal's sleeping action
        """
        return f"{self.name} is sleeping"


class Cow(Animal):
    """A class representing a Cow, which inherits from Animal."""

    def speak(self):
        """Make the cow speak with its default sound."""
        return super().speak("Moo!")

    def eat(self):
        """Make the cow eat its default food."""
        return super().eat("grass")


class Pig(Animal):
    """A class representing a Pig, which inherits from Animal."""

    def speak(self):
        """Make the pig speak with its default sound."""
        return super().speak("Oink!")

    def eat(self):
        """Make the pig eat its default food."""
        return super().eat("slop")

    def roll_in_mud(self):
        """
        Make the pig roll in mud.

        Returns:
            str: Formatted string with the pig's mud-rolling action
        """
        return f"{self.name} is rolling in mud"


class Sheep(Animal):
    """A class representing a Sheep, which inherits from Animal."""

    def speak(self):
        """Make the sheep speak with its default sound."""
        return super().speak("Baa!")

    def eat(self):
        """Make the sheep eat its default food."""
        return super().eat("grass")

    def grow_wool(self):
        """
        Make the sheep grow wool.

        Returns:
            str: Formatted string with the sheep's wool-growing action
        """
        return f"{self.name} is growing wool"

    def run(self):
        """
        Make the sheep run.

        Returns:
            str: Formatted string with the sheep's running action
        """
        return f"{self.name} is running"


def create_animal_farm():
    """
    Create a farm with various animals.

    Returns:
        list: A list of animal instances
    """
    return [Cow("Daisy", 3), Pig("Babe", 2), Sheep("Wooly", 4)]


def demonstrate_oop_concepts():
    """
    Demonstrate various OOP concepts with examples.

    Returns:
        dict: A dictionary with demonstration results
    """
    # Create dog instances
    buddy = Dog("Buddy", 9)
    miles = JackRussellTerrier("Miles", 4)

    # Create rectangle and square instances
    rectangle = Rectangle(3, 4)
    square = Square(4)

    # Create farm animals
    farm_animals = create_animal_farm()

    return {
        "dog_description": str(buddy),
        "dog_speech": miles.speak(),
        "rectangle_area": rectangle.area(),
        "square_area": square.area(),
        "farm_animals": [str(animal) for animal in farm_animals],
        "animal_sounds": [animal.speak() for animal in farm_animals],
    }


class Point(namedtuple("Point", ["x", "y"])):
    """
    A class representing a Point in 2D space using a namedtuple.

    Attributes:
        x (float): The x-coordinate of the point
        y (float): The y-coordinate of the point
    """

    def distance_to_origin(self):
        """
        Calculate the distance from this point to the origin.

        Returns:
            float: The distance to the origin
        """
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to_point(self, other):
        """
        Calculate the distance from this point to another point.

        Args:
            other (Point): Another point

        Returns:
            float: The distance between the two points
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
