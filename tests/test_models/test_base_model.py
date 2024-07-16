Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from models.base_model import BaseModel
>>> 
>>> my_model = BaseModel()
>>> my_model.name = "My First Model"
>>> my_model.my_number = 89
>>> print(my_model)
[BaseModel] (a1b548ea-53d5-451c-8510-54975affd3d5) {'id': 'a1b548ea-53d5-451c-8510-54975affd3d5', 'created_at': datetime.datetime(2024, 5, 20, 4, 52, 44, 308830), 'updated_at': datetime.datetime(2024, 5, 20, 4, 52, 44, 308814), 'name': 'My First Model', 'my_number': 89}
>>> my_model.save()
>>> print(my_model)
[BaseModel] (a1b548ea-53d5-451c-8510-54975affd3d5) {'id': 'a1b548ea-53d5-451c-8510-54975affd3d5', 'created_at': datetime.datetime(2024, 5, 20, 4, 52, 44, 308830), 'updated_at': datetime.datetime(2024, 5, 20, 4, 52, 44, 308830), 'name': 'My First Model', 'my_number': 89}
>>> my_model_json = my_model.to_dict()
>>> print(my_model_json)
{'id': 'a1b548ea-53d5-451c-8510-54975affd3d5', 'created_at': '2024-05-20T04:52:44.308830', 'updated_at': '2024-05-20T04:52:44.308830', 'name': 'My First Model', 'my_number': 89, '__class__': 'BaseModel'}
>>> print("JSON of my_model:")
JSON of my_model:
>>> for key in my_model_json.keys():
...     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
... 
        id: (<class 'str'>) - a1b548ea-53d5-451c-8510-54975affd3d5
        created_at: (<class 'str'>) - 2024-05-20T04:52:44.308830
        updated_at: (<class 'str'>) - 2024-05-20T04:52:44.308830
        name: (<class 'str'>) - My First Model
        my_number: (<class 'int'>) - 89
        __class__: (<class 'str'>) - BaseModel
