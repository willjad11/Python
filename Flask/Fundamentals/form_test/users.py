class UserDatabase:
    def __init__(self):
        pass

    error = False

    errormsg = ""

    data = {}


class User:
    def __init__(self, username, loggedin):
        self.username = username
        self.loggedin = loggedin