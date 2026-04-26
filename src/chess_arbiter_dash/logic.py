import berserk

def is_token_valid(tokenstr):
    client = berserk.Client(berserk.TokenSession(tokenstr))
    try:
        client.account.get()
        return True
    except:
        return False

def is_username_valid(p1, p2):
    print
    