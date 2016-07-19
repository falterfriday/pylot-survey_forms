"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import Flask, render_template, request, redirect, session

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

    def index(self):
        if not session.has_key('hide'):
            session['hide'] = True
        hide = session['hide']
        return render_template('index.html', hide=hide)
    
    def process(self):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/result')   

    def result(self):
        if not session.has_key('count'):
            session['count'] = 1
        else:
            session['count'] += 1        
        name = session['name']
        location = session['location']
        language = session['language']
        comment = session['comment']

        return render_template('result.html', hide=session['hide'], count=session['count'], name=name, location=location,language=language,comment=comment)