from ..dao import *

async def details_existance_check(details_to_check):
    username_check = await dao_get_username(details_to_check.username)

    if username_check: # RUSSELL REDO THIS!!!
        pass   # RUSSELL REDO THIS!!!!


async def service_create_user(user_object, new_user):
    print("ENTERED SERVICE")    
    
    data = await dao_get_username(user_object, new_user["username"])

    json_data = {
    'id': data.id,
    'username': data.username,
    'email': data.email,
    'password': data.password,
    'created_at': data.created_at,
    'last_modified': data.last_modified
    }

    return json_data

    # user_exists = await details_existance_check(new_user)

    # if user_exists != "success":
    #     return user_exists
