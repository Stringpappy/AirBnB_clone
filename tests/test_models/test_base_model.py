Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from models.base_model import BaseModel
>>> 
>>> my_model = BaseModel()
>>> my_model.name = "My First Model"
>>> my_model.my_number = 89
>>> my_model.my_number = 89
>>> print(my_model)
[BaseModel] (a6d72a00-9457-4aa7-ab36-49c61aeee188) {'id': 'a6d72a00-9457-4aa7-ab36-49c61aeee188', 'created_at': datetime.datetime(2024, 7, 16, 6, 14, 24, 873261), 'updated_at': datetime.datetime(2024, 7, 16, 6, 14, 24, 873240), 'name': 'My First Model', 'my_number': 89}
>>> my_model_json = my_model.to_dict()
>>> print(my_model_json)
{'id': 'a6d72a00-9457-4aa7-ab36-49c61aeee188', 'created_at': '2024-07-16T06:14:24.873261', 'updated_at': '2024-07-16T06:14:24.873240', 'name': 'My First Model', 'my_number': 89, '__class__': 'BaseModel'}
>>> print("JSON of my_model:")
JSON of my_model:
>>> for key in my_model_json.keys():
... print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
