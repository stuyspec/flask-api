from flask import render_template, flash, redirect, request, session, url_for, jsonify, make_response
from app import app, db, models



#----------------------------------------------

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

#----------------------------------------------


@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>', methods=['GET'])
def get_section_by_slug(section_slug, subsection_slug):
    if subsection_slug == "main":
        target = models.Section.query.filter(
            models.Section.slug == section_slug
        ).first()
    else:
        target = models.Subsection.query.filter(
            models.Subsection.slug == subsection_slug
        ).first()
    return jsonify({"description": target.description})

@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles/', methods=['GET'], defaults={'article_slug': None})
@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles/<string:article_slug>', methods=['GET'])
def articles_in_section(section_slug, subsection_slug, article_slug):
    if article_slug != None and article_slug != "None":
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
      "dateTime": article.datetime,
      "id": article.id,
      "isDraft": article.isDraft,
      "issue": article.issue,
      "sectionId": article.section_id,
      "slug": article.slug,
      "subsectionId": article.subsection_id,
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
      "dateTime": article.date_time,
      "id": article.id,
      "isDraft": article.is_draft,
      "issue": article.issue,
      "sectionId": article.section_id,
      "slug": article.slug,
      "subsectionId": article.subsection_id,
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
    "firstName": user.first_name,
    "id": user.id,
    "lastName": user.last_name,
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
      "dateTime": article.date_time,
      "id": article.id,
      "isDraft": article.is_draft,
      "issue": article.issue,
      "sectionId": article.section_id,
      "slug": article.slug,
      "subsectionId": article.subsection_id,
      "title": article.title,
      "volume": article.volume
                    }
        secure_articles.append(article_dict)
    limit = request.args.get('limit')
    if limit is not None:
        secure_articles = secure_articles[:int(limit)]
    return jsonify( {"articles": secure_articles} )
#----------------------------------------------
