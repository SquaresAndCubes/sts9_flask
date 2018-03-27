from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
import datetime
sts9 = Flask(__name__, )

#bootstrap css object
bootstrap = Bootstrap(sts9)

#sts9 db connection#
sts9.config['MONGO_HOST'] = '10.0.0.36'
sts9.config['MONGO_PORT'] = 27017
sts9.config['MONGO_DBNAME'] = 'sts9_db'
sts9_db = PyMongo(sts9, config_prefix='MONGO')

#Global Variables
now = datetime.datetime.now()

#Home Page#
@sts9.route('/')
def home():
    return render_template('home.html')

#SETLISTS#
@sts9.route('/setlists')
@sts9.route('/setlists/<year>')
def setlists(year=None):
    #finds all distinct years, for year navbar
    years = sts9_db.db.setlists.distinct('year')
    while True:
        #set to most recent setlists as landing page
        if year == None:
            year = years[0]
            break
        #verify if it is a valid year url
        elif year in years:
            break
        elif year not in years:
            return render_template('404.html')
    #render setlists template
    setlists = sts9_db.db.setlists.find({'year': year})
    return render_template('setlists_nav.html', years=years, setlists=setlists, year=year)


    #object for current year shows

#SONGS#
@sts9.route('/songs')
def songs():
    #figure out how to get the song occurance totals in a list
    songs = sorted(sts9_db.db.setlists.distinct('setlist'))
    return render_template('songs.html', songs=songs)

#404 - Page Not Found Error Handler#
@sts9.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    sts9.run(debug=True)
