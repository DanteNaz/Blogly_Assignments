




from flask import Flask, request, redirect, render_template
from models import db, connect_db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)









@app.route("/")
def list_users():
    """List users and show create users form."""

    users = User.query.all()
    return render_template("list.html", users=users)






@app.route("/add_user", methods=["POST"])
def add_user():
    """Add user and redirect to list."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")







@app.route("/<int:user_id>")
def show_user(user_id):
    """Show info on a singular user."""

    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)









@app.route("/user_edit/<int:user_id>", methods=['GET'])
def edit_user_page(user_id):
    """Edit a User's Details"""

    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)







@app.route("/user_edit/<int:user_id>/editing", methods=['POST'])
def edit_user(user_id):
    """Edit a User's Details"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    User.query.filter_by(id=user_id).delete()
    db.session.add(user)
    db.session.commit()


    return redirect("/")









@app.route("/user_delete/<int:user_id>", methods=['GET', 'DELETE'])
def delete_user(user_id):
    """Delete a User"""


    User.query.filter_by(id=user_id).delete()

    db.session.commit()

    return redirect('/')










#____________________________________________________________________________________________________________



# @app.route("/user_edit/<int:user_id>/editing", methods=['POST'])
# def edit_user(user_id):
#     """Edit a User's Details"""

#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     image_url = request.form['image_url']

#     user = User(first_name=first_name, last_name=last_name, image_url=image_url)

#     User.query.filter_by(id=user_id).delete()

#     db.session.commit()


#     return redirect("/")
