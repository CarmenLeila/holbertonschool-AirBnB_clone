#!/usr/bin/python3
""" Creates a BaseModel """

import uuid
from datetime import datetime

class BaseModel:
    """ class of Base Model """


    def __init__(self , *args, **kwargs):
        """ 
        Initialization of instance attributes
        Args:
                args: set of arguments
                kwargs: set of arguments with keywords
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
    def __str__(self):
        """ Representation String of instance """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name,self.id,self.__dict__)
    def save(self):
        """ Updates the public instance """
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.save()
        
    def to_dict(self):
        """ Returns an instance dictionary """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
