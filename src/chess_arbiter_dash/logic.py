import berserk

def is_token_valid(tokenstr):
    client = berserk.Client(berserk.TokenSession(tokenstr))
    try:
        client.account.get()
        return True
    except:
        return False

def is_username_valid(tokenstr, p1, p2):
    session = berserk.TokenSession(tokenstr)
    client = berserk.Client(session=session)

    try:
        client.users.get_public_data(p1)
        client.users.get_public_data(p2)
        return True
    except:
        return False