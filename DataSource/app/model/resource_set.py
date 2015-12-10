from app import db

__author__ = 'Xiaoxiao.Xiong'

class ResourceSet(db.Model):
    """
    Resource Set, which can include multiple categories
    """
    __tablename__  = 'ResourceSet'

    id     = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # name   = db.Column(db.String(50),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('UserAccount.id'), nullable=False)
    rs_id  = db.Column(db.String(100),nullable=True)

    user = db.relationship('UserAccount')

    def __init__(self, user_id, rs_id):

        # self.name    = kwargs['name']
        self.user_id = user_id
        self.rs_id   = rs_id

    @property
    def serialize(self):
        """

        :return:
        """
        return {

        }

