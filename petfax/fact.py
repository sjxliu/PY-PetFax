from flask import (Blueprint, render_template, request)

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=['GET','POST'])
def index():
    if request == 'POST':
        print(request.form)
        return redirect ('/facts')

    return 'this is the facts index'
        
#     return render_template('facts/index.html')

# bp.route('/new')
# def new ():
#     return render_template('facts/new.html')