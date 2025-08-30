import pytest
from src.oop_utils import (
    Dog,
    JackRussellTerrier,
    Rectangle,
    Square,
    Animal,
    Cow,
    Pig,
    Sheep,
    Point,
)


def test_dog_creation():
    """Test Dog class instantiation and attributes."""
    dog = Dog("Buddy", 5)

    assert dog.name == "Buddy"
    assert dog.age == 5
    assert dog.species == "Canis familiaris"


def test_dog_str_method():
    """Test Dog class __str__ method."""
    dog = Dog("Buddy", 5)

    assert str(dog) == "Buddy is 5 years old"


def test_dog_speak_method():
    """Test Dog class speak method."""
    dog = Dog("Buddy", 5)

    assert dog.speak("Woof!") == "Buddy says Woof!"


def test_jack_russell_terrier_inheritance():
    """Test JackRussellTerrier inheritance from Dog."""
    jack = JackRussellTerrier("Miles", 4)

    assert isinstance(jack, Dog)
    assert jack.name == "Miles"
    assert jack.age == 4


def test_jack_russell_terrier_speak():
    """Test JackRussellTerrier speak method with default sound."""
    jack = JackRussellTerrier("Miles", 4)

    assert jack.speak() == "Miles says Arf"
    assert jack.speak("Grrr") == "Miles says Grrr"


def test_rectangle_area():
    """Test Rectangle area calculation."""
    rect = Rectangle(3, 4)

    assert rect.area() == 12


def test_rectangle_perimeter():
    """Test Rectangle perimeter calculation."""
    rect = Rectangle(3, 4)

    assert rect.perimeter() == 14


def test_rectangle_is_square():
    """Test Rectangle is_square method."""
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(5, 5)

    assert not rect1.is_square()
    assert rect2.is_square()


def test_square_inheritance():
    """Test Square inheritance from Rectangle."""
    square = Square(4)

    assert isinstance(square, Rectangle)
    assert square.side_length == 4
    assert square.length == 4
    assert square.width == 4


def test_square_area():
    """Test Square area calculation."""
    square = Square(4)

    assert square.area() == 16


def test_animal_creation():
    """Test Animal class instantiation."""
    animal = Animal("Generic", 2)

    assert animal.name == "Generic"
    assert animal.age == 2


def test_animal_methods():
    """Test Animal class methods."""
    animal = Animal("Generic", 2)

    assert animal.speak("Meow") == "Generic says Meow"
    assert animal.eat("food") == "Generic is eating food"
    assert animal.sleep() == "Generic is sleeping"


def test_cow_inheritance():
    """Test Cow inheritance from Animal."""
    cow = Cow("Daisy", 3)

    assert isinstance(cow, Animal)
    assert cow.speak() == "Daisy says Moo!"
    assert cow.eat() == "Daisy is eating grass"


def test_pig_inheritance():
    """Test Pig inheritance from Animal."""
    pig = Pig("Babe", 2)

    assert isinstance(pig, Animal)
    assert pig.speak() == "Babe says Oink!"
    assert pig.eat() == "Babe is eating slop"
    assert pig.roll_in_mud() == "Babe is rolling in mud"


def test_sheep_inheritance():
    """Test Sheep inheritance from Animal."""
    sheep = Sheep("Wooly", 4)

    assert isinstance(sheep, Animal)
    assert sheep.speak() == "Wooly says Baa!"
    assert sheep.eat() == "Wooly is eating grass"
    assert sheep.grow_wool() == "Wooly is growing wool"
    assert sheep.run() == "Wooly is running"


def test_point_creation():
    """Test Point class instantiation."""
    point = Point(3, 4)

    assert point.x == 3
    assert point.y == 4


def test_point_distance_methods():
    """Test Point distance calculation methods."""
    point1 = Point(3, 4)
    point2 = Point(0, 0)
    point3 = Point(6, 8)

    assert point1.distance_to_origin() == 5.0
    assert point1.distance_to_point(point2) == 5.0
    assert point1.distance_to_point(point3) == 5.0
