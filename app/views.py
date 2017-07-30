from flask import render_template, flash, redirect, request, session, url_for, jsonify, make_response
from app import app, db, models
import datetime



#----------------------------------------------    

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

#----------------------------------------------


@app.route('/get_section_by_slug/sections/<string:section_slug>/subsection/<string:subsection_slug>', methods=['GET'])
def return_description(section_slug,subsection_slug):
    if subsection_slug == "main":
        target = models.Section.query.filter(
            models.Section.slug == section_slug
                ).first()
    else:
        target = models.Subsection.query.filter(
            models.Subsection.slug == subsection_slug
                ).first()
    return jsonify({"description": target.description})

@app.route('/get_section_articles/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles/', methods=['GET'], defaults={'article_slug': None}) 
@app.route('/get_section_articles/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles/<string:article_slug>', methods=['GET']) 
def articles_in_section(section_slug,subsection_slug,article_slug):
    if article_slug is not None and article_slug is not "None":
        articles = [models.Article.query.filter(
            models.Article.slug == article_slug
                ).first()]
    elif subsection_slug == "main":
        section =  models.Section.query.filter(
            models.Section.slug == section_slug
                ).first()
        articles = models.Article.query.filter(
            models.Article.section == section
                ).all()
    else:
        subsection =  models.Subsection.query.filter(
            models.Subsection.slug == subsection_slug
                ).first()
        articles = models.Article.query.filter(
            models.Article.subsection == subsection
                ).all()
    secure_articles = []
    for article in articles:
        article_dict = {
      "content": article.content, 
      "datetime": article.datetime, 
      "id": article.id, 
      "isDraft": article.isDraft, 
      "issue": article.issue, 
      "section_id": article.section_id, 
      "slug": article.slug, 
      "subsection_id": article.subsection_id, 
      "title": article.title, 
      "volume": article.volume
                    }   
        secure_articles.append(article_dict)
    return jsonify({"articles": secure_articles})


#----------------------------------------------    

@app.route('/newspaper/<int:volume>/<int:issue>', methods=['GET'])
def retrieve_article_data(volume,issue):
    articles = models.Article.query.filter(models.Article.volume == volume 
        and models.Article.issue == issue).all()
    secure_articles = []
    for article in articles:
        article_dict = {
      "content": article.content, 
      "datetime": article.datetime, 
      "id": article.id, 
      "isDraft": article.isDraft, 
      "issue": article.issue, 
      "section_id": article.section_id, 
      "slug": article.slug, 
      "subsection_id": article.subsection_id, 
      "title": article.title, 
      "volume": article.volume
                    }   
        secure_articles.append(article_dict)
    issuu_code = models.Issuu.query.filter(models.Issuu.volume == volume 
        and models.Issuu.issue == issue).first().code
    return jsonify({"issuu_code": issuu_code, "articles": secure_articles})

@app.route('/user/<int:user_id>', methods=['GET'])
def retrieve_user_data(user_id):
    user =  models.User.query.get(user_id)
    user_data = {
    "description": user.description, 
    "email": user.email, 
    "firstname": user.firstname, 
    "id": user.id, 
    "lastname": user.lastname, 
    "password": user.password, 
    "username": user.username
  }
    return jsonify( {"user_data": user_data} )

@app.route('/list_articles/articles/', methods=['GET'])
def all_articles():
    articles = models.Article.query.all()
    secure_articles = []
    for article in articles:
        article_dict = {
      "content": article.content, 
      "datetime": article.datetime, 
      "id": article.id, 
      "isDraft": article.isDraft, 
      "issue": article.issue, 
      "section_id": article.section_id, 
      "slug": article.slug, 
      "subsection_id": article.subsection_id, 
      "title": article.title, 
      "volume": article.volume
                    }   
        secure_articles.append(article_dict)
    limit = request.args.get('limit')
    if limit is not None:
        secure_articles = secure_articles[:int(limit)]
    return jsonify( {"articles": secure_articles} )
#---------------------------------------------- POST endpoints
def find_section_of_article(section_name):
  section = models.Section.query.filter(models.Section.name==section_name).first()
  if section == None:
    return None
  else:
    return section
@app.route('/create_article/articles', methods=['POST'])
def create_article():
  article = models.Article(title = request.form["title"],
                           slug = request.form["slug"],
                           content = request.form["content"],
                           datetime = datetime.datetime.utcnow(),
                           volume = int(request.form["volume"]),
                           issue = int(request.form["issue"]),
                           isDraft = request.form["isDraft"],
                           section = find_section_of_article(request.form["section"]),
                           subsection = None) #remove this after section and subsection become part of the same model
  db.session.add(article)
  db.session.commit()
  return jsonify({"status":"Article has been added"})
@app.route('/create_section/sections/', methods=['POST'])
def create_section():
  section = models.Section(name= request.form["name"],
                           slug= request.form["slug"],
                           description= request.form["description"])
  db.session.add(section)
  db.session.commit()
  return jsonify({"Status": "Section has been sucessfully added"})
#---------------------------------------------- DELETE endpoints
@app.route('/delete_section/sections/<string:section_slug>', methods =['DELETE'])
def delete_section(section_slug):
  section = models.Section.query.filter_by(slug=section_slug).first()
  db.session.delete(section)
  db.session.commit()
  return jsonify({"Status":"Section has been deleted"})
@app.route('/delete_article/articles/<string:article_slug>', methods = ['DELETE'])
def delete_article(article_slug):
  article = models.Article.query.filter_by(slug = article_slug).first()
  db.session.delete(article)
  db.session.commit()
  return jsonify({"Status":"Article has been deleted"})
#---------------------------------------------- PUT endpoints
@app.route('/update_section/sections/<string:section_slug>', methods =['PUT'])
def update_section(section_slug):
  section = models.Section.query.filter_by(slug=section_slug).first()
  if request.form['name'] is not None:
    section.name = request.form['name']
  if request.form['slug'] is not None:
    section.slug = request.form['slug']
  if request.form['description'] is not None:
    section.description = request.form['description']
  db.session.commit()
  return jsonify({"Status":"Section has been updated"})
@app.route('/update_article/articles/<string:article_slug>', methods =['PUT'])
def update_article(article_slug):
  article = models.Article.query.filter_by(slug = article_slug).first()
  if request.form['title'] is not None:
    article.title = request.form['title']
  if request.form['slug'] is not None:
    article.slug = request.form['slug']
  if request.form['content'] is not None:
    article.content = request.form['content']
  if request.form['volume'] is not None:
    article.volume = request.form['volume']
  if request.form['issue'] is not None:
    article.issue = request.form['issue']
  if request.form['isDraft'] is not None:
    article.isDraft = request.form['isDraft']
  if request.form['section'] is not None:
    article.section = find_section_of_article(request.form['section'])
  article.datetime = datetime.datetime.utcnow()
  db.session.commit()
  return jsonify({"Status":"Article has been updated"})
#---------------------------------------------- 
