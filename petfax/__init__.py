from  flask import Flask


def create_app():
    app = Flask(__name__)


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


    from . import pet
    from . import fact

    
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    return app

