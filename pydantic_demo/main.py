"""
pydantic
Benefits:
    - IDE type hint
    - Data Validation
    - JSON Serialisation

"""
"""
------------------------------------------------
                   pydantic         dataclass
------------------------------------------------
Type hints           yes                yes
------------------------------------------------
Data Validation      yes                No
------------------------------------------------
Serialisation        yes                /!\
------------------------------------------------
Built-in             No                 yes
------------------------------------------------

 """
from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr # Data Validation
    acount_id: int


    # custom validation
    @field_validator("acount_id")
    def validator_acount_id(cls, value: int)->int:
        if value <= 0:
            raise ValueError(f"value must be positive {value}")
        else:
            return value
        
 

user_data = {"name": "jack", "email": "dr4@orannge.fr", "acount_id": 4}

# =============  read data ================

user = User(name="jack", email="dr4@orange.fr", acount_id=1234)

# or this way

user = User(**user_data)

# - JSON Serialisation
user_json_str=user.json()
# dict object
user_dict_obj=user.dict()
# convert json str to pandatic model
json_str = '{"name":"jack","email":"dr4@orannge.fr","acount_id":4}'
user_model_from_json = User.parse_raw(json_str)

if __name__ == "__main__":
    print(user.acount_id)
    print(user_json_str)
    print(user_dict_obj)
    print(user_model_from_json.name)
    
