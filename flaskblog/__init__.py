import inspect                                                              
import pkgutil                                                                 
import importlib                                                               
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# secret keys help protect the forms from modifying cookies, cross-site request forgery attack
app.config['SECRET_KEY'] = '6fa73538fe5688211055ed30dd556b17'

# location of thr uri of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes


def import_models():                                                           
    thismodule = sys.modules[__name__]                                         

    for loader, module_name, is_pkg in pkgutil.iter_modules(                   
            thismodule.__path__, thismodule.__name__ + '.'):                   
        module = importlib.import_module(module_name, loader.path)             
        for name, _object in inspect.getmembers(module, inspect.isclass):      
            globals()[name] = _object                                                                                     

import_models()  