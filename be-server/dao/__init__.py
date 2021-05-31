async def dao_get_username(user_object, username):
    print("ENTERED DAO")

    result = user_object.query.filter_by(username=username).first()

    print(result)

    return result