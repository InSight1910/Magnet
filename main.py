"""
DO NOT EDIT THIS FILE, IT'S NOT PART OF THE TEST.
If you edit this file your application will be automatically rejected.
"""
# standard library
from getpass import getpass

# utils
from utils import auth

# functions to be implement
from models import DogHouse




def main():
    """
    This file should not be modified. This should be executed
    without throwing any exceptions. To do this, you must complement
    the DogHouse class found in the models.py file
    """
    # get credentials
    email = input('What\'s is your email? ')
    password = getpass('What\'s is your password? ')
    
    credentials = {
        'email': email,
        'password': password,
    }

    # get token
    token = auth(**credentials)

    # create dog house and pull data from api
    dog_house = DogHouse()
    dog_house.get_data(token=token)

    # results
    total_breeds = dog_house.get_total_breeds()
    total_dogs = dog_house.get_total_dogs()
    common_breed = dog_house.get_common_breed()
    common_dog_name = dog_house.get_common_dog_name()
    

    # print requested data
    
    print('Total breeds: {}'.format(total_breeds))
    print('Total dogs: {}'.format(total_dogs))
    print('Most common breed name: {}'.format(common_breed))
    print('Most common dog name: {}'.format(common_dog_name))
    

    data = {
        'total_breeds': total_breeds,
        'total_dogs': total_dogs,
        'common_breed': common_breed.name,
        'common_dog_name': common_dog_name,
    }
    dog_house.send_data(data=data, token=token)
 

if __name__ == '__main__':
    main()
