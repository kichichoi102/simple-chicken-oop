from src.collections.farm import Farm
from src.single_entities.chicken import Chicken
from src.single_entities.cow import Cow
from src.single_entities.pig import Pig


if __name__ == "__main__":
    # Instantiate Farm and one animal each
    farm = Farm()
    henrietta = Chicken("Henrietta", 1)
    bessie = Cow("Bessie", 3)
    mimi = Pig("Mimi", 2)

    # Add animals to farm
    farm.add_animal(henrietta)
    farm.add_animal(bessie)
    farm.add_animal(mimi)

    farm.list_animals()

