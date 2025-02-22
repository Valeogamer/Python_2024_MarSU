from typing import TypedDict, List, Union, Optional, Dict

class AnimalData(TypedDict):
    my_obj: 'MyObj'
    pets: List[Union['Cat', 'Dog']]

AD = Optional[Dict['MyObj', List[Union['Cat', 'Dog']]]]

class MyObj:
    pass

class Cat:
    pass

class Dog:
    pass

def process_animal_data(data: AnimalData) -> None:
    pass