# simple-chicken-oop
This repo demonstrates the simple implementation of OOP principles including the 4 pillars.

[Documentation Link](https://docs.google.com/document/d/1d3POQjeTx4FpnYwPIogbDZY74NMiMPsBaIAlBNu410I/edit?usp=sharing)

## Note:
This repository does not follow any best practices on naming conventions, branching conventions, or PEP conventions. It is a very quick and dirty implementation to demonstrate the basic concepts of OOP including the four pillars.

The other repo: [`chicken-oop`](https://github.com/kichichoi102/chicken-oop) practices the best practices, and extends this repository with SOLID principles and OOD.

## OOP Concepts used:
```
1. Encapsulation
The Animal class encapsulates the name and age properties and 
the make_sound behavior.

2. Inheritance
The single entity classes inherit from the Animal class and 
have their own implementation of the make_sound method.

3. Polymorphism
The Farm class can work with different types of animals, 
as long as they have a name property. The list_animals method 
can be called on any object that has a list of animals.

4. Abstraction
The Animal class is an abstract class, since it defines a 
method (make_sound) that must be implemented by its subclasses.
```

In this example, the Animal class is the parent class and has two properties (name and age) and a method (make_sound) 
that must be implemented by its child classes. The single entity classes inherit from the Animal class and 
implement their own version of the make_sound method. e.g. chicken: cock-a-doodle-doo, cow: moo

The Farm class is an example of polymorphism, as it can work with any type of animal that has a name property. 
The list_animals method can be called on any object that has a list of animals.

## File Structure
```
.
├── LICENSE
├── README.md
├── main.py
└── src
    ├── collections
    │   └── farm.py
    ├── interfaces
    │   └── animal.py
    └── single_entities
        ├── chicken.py
        ├── cow.py
        └── pig.py
```

## Prerequisites:
- python3

## Usage:
- `python3 main.py`

## Expected Output:
```python
Name: Henrietta Age: 1
Name: Bessie Age: 3
Name: Mimi Age: 2
```

