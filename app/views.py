from flask import render_template, flash, redirect, request, session, url_for, jsonify
from app import app, db, models

from app.utils.authentication import authenticate, get_user


#----------------------------------------------    

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

#----------------------------------------------

@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>', methods=['GET'])
def return_descpt(section_slug,subsection_slug):
    return 

@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles', methods=['GET'])
def articles_within(section_slug,subsection_slug):
    return 

@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles/<string:article_slug>', methods=['GET'])
def requested_article(section_slug,subsection_slug):
    return 

#----------------------------------------------    
