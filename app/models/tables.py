from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String,unique = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)

    def __init__(self,username,password,name,email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '<id: %s>'%id

class Post(db.Model):
    __tablename__ = 'post'

    id  = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.Text)
    id_user = db.Column(db.Intenger,db.ForeignKey('user.id'))

    user = db.relationship('User', foreign_keys = id_user)

    def __init__(self,content,id_user):
        self.content = content
        self.id_user = id_user

    def __repr__(self):
        return '<Post %r>' %self.id

class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Column(db.Integer,primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
    id_follower = db.Column(db.Intener,db.ForeignKey('users.id'))

    user  = db.relationship('User',foreign_keys=id_user)
    follow = db.relationship('User',foreign_keys=id_follower)

