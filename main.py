from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
sts9 = Flask(__name__, )

bootstrap = Bootstrap(sts9)

#sts9 db connection#
sts9.config['MONGO_HOST'] = '10.0.0.36'
sts9.config['MONGO_PORT'] = 27017
sts9.config['MONGO_DBNAME'] = 'sts9_db'
sts9_db = PyMongo(sts9, config_prefix='MONGO')

#SETLISTS#
@sts9.route('/setlists')
def setlists():
    setlists_data = sts9_db.db.setlists.find()
    return render_template('setlists_nav.html', setlists_data=setlists_data)

#404 - Page Not Found Error Handler#
@sts9.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    sts9.run(debug=True)
