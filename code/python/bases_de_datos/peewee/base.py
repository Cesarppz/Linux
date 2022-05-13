import peewee



class User(peewee.Model):
    user_name = peewee.CharField(max=50, unique=True, index=True)


    class Meta:
        def __init__(self, database):
            self.database = database
        database = database