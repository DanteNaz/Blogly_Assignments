



from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()                                                    

def connect_db(app):
    db.app = app                                                                           
    db.init_app(app)




# MODELS ARE BELOW!


class User(db.Model):

    __tablename__ = 'users'





    def __repr__(self):
        u = self
        return f"<user_id={u.id}, first_name={u.first_name}, last_name={u.last_name}, image_url={u.image_url}>"




    id = db.Column(db.Integer,                            
                    primary_key = True,                           
                    autoincrement = True)                                
                                                                
    first_name = db.Column(db.String(20),                             
                        nullable = False,                            
                        unique = False)                               

    last_name = db.Column(db.String(20),                             
                        nullable = False,                            
                        unique = False)


    image_url = db.Column(db.String, nullable=False)




