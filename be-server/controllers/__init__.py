from flask import json
from ..services import *

async def controller_create_user(user_object, json_data):
    print("ENTERED CONTROLLER")

    try:
        data = await service_create_user(user_object, json_data)
        return data

    except Exception as e:
        return str(e)