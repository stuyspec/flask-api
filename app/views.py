from flask import request, jsonify, make_response

from app import flask_api, models


# ----------------------------------------------  Error Handlers


@flask_api.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@flask_api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# ---------------------------------------------- Section and Article Endpoints

SECTION_ROUTE = "/sections/<string:section_slug>/" \
                "subsection/<string:subsection_slug>"

SECTION_ARTICLES_ROUTE = "%s/articles" % SECTION_ROUTE

SECTION_ARTICLE_ROUTE = "%s/<string:article_slug>" % SECTION_ARTICLES_ROUTE

ALL_ARTICLES_ROUTE = "/articles"


@flask_api.route(SECTION_ROUTE)
def get_section_by_slug(section_slug, subsection_slug):
    if subsection_slug == "main":
        target = models.Section.query.filter(
            models.Section.slug == section_slug
        ).first()
        return jsonify({"description": target.description})
    else:
        target = models.Subsection.query.filter(
            models.Subsection.slug == subsection_slug
        ).first()
        if target.parent_slug == section_slug:
            return jsonify({"description": target.description})


@flask_api.route(SECTION_ARTICLES_ROUTE, defaults={'article_slug': None})
@flask_api.route(SECTION_ARTICLE_ROUTE)
def get_section_articles(section_slug, subsection_slug, article_slug):
    if article_slug is not None and article_slug is not "None":
        articles = [models.Article.query.filter(
            models.Article.slug == article_slug
        ).first()]
    elif subsection_slug == "main":
        section = models.Section.query.filter(
            models.Section.slug == section_slug
        ).first()
        articles = models.Article.query.filter(
            models.Article.section == section
        ).all()
    else:
        subsection = models.Subsection.query.filter(
            models.Subsection.slug == subsection_slug
        ).first()
        articles = models.Article.query.filter(
            models.Article.subsection == subsection
        ).all()
    secure_articles = []
    for article in articles:
        article_dict = {
            "content": article.content,
            "datetime": article.date_time,
            "id": article.id,
            "isDraft": article.is_draft,
            "issue": article.issue,
            "sectionId": article.section_id,
            "slug": article.slug,
            "title": article.title,
            "volume": article.volume
        }
        secure_articles.append(article_dict)
    return jsonify({"articles": secure_articles})


@flask_api.route('/newspaper/<int:volume>/<int:issue>')
def get_issue_articles(volume, issue):
    articles = models.Article.query.filter(models.Article.volume == volume
                                           and models.Article.issue == issue).all()
    # Container for articles that have
    # been converted to a dictionary to display data
    converted_articles = []
    for article in articles:
        article_dict = {
            "content": article.content,
            "datetime": article.date_time,
            "id": article.id,
            "is_draft": article.is_draft,
            "issue": article.issue,
            "section_id": article.section_id,
            "slug": article.slug,
            "title": article.title,
            "volume": article.volume
        }
        converted_articles.append(article_dict)
    issuu_code = models.Issuu.query.filter(models.Issuu.volume == volume
                                           and models.Issuu.issue == issue).first().code
    return jsonify({"issuu_code": issuu_code, "articles": secure_articles})


@flask_api.route(ALL_ARTICLES_ROUTE)
def get_all_articles():
    articlesInIssue = models.Article.query.all()
    secure_articles = []
    for article in articlesInIssue:
        article_dict = {
            "content": article.content,
            "datetime": article.date_time,
            "id": article.id,
            "is_draft": article.is_draft,
            "issue": article.issue,
            "section_id": article.section_id,
            "slug": article.slug,
            "title": article.title,
            "volume": article.volume
        }
        secure_articles.append(article_dict)
    limit = request.args.get('limit')
    if limit is not None:
        secure_articles = secure_articles[:int(limit)]
    return jsonify({"articles": secure_articles})


# ---------------------------------------------- User data endpoints


@flask_api.route('/user/<int:user_id>')
def get_user(user_id):
    user = models.User.query.get(user_id)
    user_data = {
        "description": user.description,
        "email": user.email,
        "firstName": user.firstname,
        "id": user.id,
        "lastName": user.lastname,
        "username": user.username
    }
    return jsonify({"user_data": user_data})

# ----------------------------------------------
