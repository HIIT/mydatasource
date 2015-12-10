

from app import db

__author__ = 'Xiaoxiao.Xiong'

class UserAccount(db.Model):
    """
    Account
    """
    __tablename__  = 'UserAccount'



    id           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username     = db.Column(db.String(50),nullable=False)
    password     = db.Column(db.String(64),nullable=False)
    user_info_id = db.Column(db.Integer,db.ForeignKey('UserInfo.id'), nullable=False)
    status       = db.Column(db.Integer,nullable=False)
    ext_id       = db.Column(db.String(100),nullable=False)

    user_info = db.relationship('UserInfo')

    def __init__(self,**kwargs):

        self.username  = kwargs['username']
        self.password  = kwargs['password']
        self.user_info = kwargs['user_info_id']
        self.status    = kwargs['status']
        self.ext_id    = kwargs['ext_id']