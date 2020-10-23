# utils
from utils import get
from utils import post

# typing
from typing import List

import requests
import json
import statistics 
from statistics import mode 


class Dog(object):
    """
    Dog object that is composed of the id, name and breed of the dog

    To initialize:
    :param id: dog id
    :param name: dog name
    :param breed: dog breed id

    USAGE:
        >>> dog = Dog(id=1, name='Bobby', breed=1)
    """
    def __init__(self, id: int, name: str, breed: int):
        self.id = id
        self.name = name
        self.breed = breed
    



class Breed(object):
    """
    Breed object that is composed of the id and the name of the breed.

    To initialize:
    :param id: breed id
    :param name: breed name

    Also, breed has a list of dogs for development purposes
    :field dogs: breed dog list

    USAGE:
        >>> breed = Breed(id=1, name='Kiltro')
        >>> dog = Dog(id=1, name='Cachupin', breed=breed.id)
        >>> breed.add_dog(dog)
        >>> breed.dogs_count()
        1
    """
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.dogs: List[Dog] = []

    def add_dog(self, dog: Dog):
        self.dogs.append(dog)

    def dogs_count(self) -> int:
        return len(self.dogs)


class DogHouse(object):
    """
    Doghouse object that manipulates information on breeds and dogs.
    We expect you implement all the methods that are not implemented
    so that the flow works correctly


    DogHouse has a list of breeds and a list of dogs.
    :field breeds: breed list
    :field dogs: dog list

    USAGE:
        >>> dog_house = DogHouse()
        >>> dog_house.get_data(token='some_token')
        >>> total_dogs = dog_house.get_total_dogs()
        >>> common_breed = dog_house.get_common_breed()
        >>> common_dog_name = dog_house.get_common_dog_name()
        >>> total_breeds = dog_house.get_total_breeds()
        >>> data = {  # add some data
        ...     'total_dogs': total_dogs,
        ...     'total_breeds': total_breeds,
        ...     'common_breed': common_breed.name,
        ...     'common_dog_name': common_dog_name,
        ... }
        >>> token = 'some token'
        >>> dog_house.send_data(data=data, token=token)
    """
    def __init__(self):
        self.breeds: List[Breed] = []
        self.dogs: List[Dog] = []

    def get_data(self, token: str):
        """
        You must get breeds and dogs data from our API: http://dogs.magnet.cl

        We recommend using the Dog and Breed classes to store
        the information, also consider the dogs and breeds fields
        of the DogHouse class to perform data manipulation.
        """
        url = "https://dogs.magnet.cl/api/v1/";
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'JWT {0}'.format(token)}
        responseDog = get(url=url+'dogs/', token=token)
        responseBreed = get(url=url+'breeds/',token=token)
        
        for da in responseDog['results']:
            dog = Dog(id=da['id'], name=da['name'], breed=da['breed'])
            self.dogs.append(dog)
        for da in responseBreed['results']:
            breed = Breed(id=da['id'], name=da['name'])

            self.breeds.append(breed)
        
        
        

    
    def get_total_breeds(self) -> int:
        """
        Returns the amount of different breeds in the doghouse
        """
        return len(self.breeds)
    def get_total_dogs(self) -> int:
        """
        Returns the amount of dogs in the doghouse
        """
        return len(self.dogs)

    def get_common_breed(self) -> Breed:
        """
        Returns the most common breed in the doghouse
        """
        
        listt = []
        for breedss in self.breeds:
            z = 0
            for dogss in self.dogs:
                if breedss.id == dogss.breed:
                    z+=1;
            data = {
                'breed': breedss,
                'amount': z
            }
            listt.append(data)
        
        
        maxAmount = 0;
        for x in listt:
            if x['amount'] >= maxAmount:
                maxAmount = x['amount']
        for x in listt:
            if maxAmount == x['amount']:
                return x['breed']

        

    def get_common_dog_name(self) -> str:
        """
        Returns the most common dog name in the doghouse
        """
        name = []
        for x in self.dogs:
            name.append(x.name)
        
        return mode(name)

    def send_data(self, data: dict, token: str):
        """
        You must send the answers obtained from the implemented
        methods, the parameters are defined in the documentation.

        Important!! We don't tell you if the answer is correct
        """
        url = "https://dogs.magnet.cl/api/v1/";
        post(url=url+'answer/',data=data, token=token)
