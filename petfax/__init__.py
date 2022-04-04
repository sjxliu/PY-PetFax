from  flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from . import models
    models.db.init_app(app)

    migrate = Migrate(app, models.db)

    from . import pet
    from . import fact

    
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app

# routing practice:

    # @app.route("/")
    # def greeting():
    #     return 'Hello, PetFax!'

    # @app.route('/login', methods = ['POST', 'GET'])
    # def login():
    #     if request.method == 'POST':
    #         user = request.form['nm']
    #         return redirect(url_for('success', name = user))
    #     else:
    #         user = request.args.get('nm')
    #         return redirect(url_for('success', name = user))

    # @app.route("/success/<username>")
    # def success(username):
    #     return f"Hello, {username}!"


    # @app.route("/post", methods = ['POST'])
    # def adoption():
    #     return 'Add pet post'

    # @app.route('/post/<int:id>')
    # def show_post(id):
    #     return f'This post has the id {id}'




