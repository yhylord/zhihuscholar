from zhihuscholar import db
from sklearn.naive_bayes import MultinomialNB
import numpy as np


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))

    feedback = db.relationship('Feedback')

    recommender = db.relationship('Recommender', back_populates='user')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def is_recommendable(self):
        return len(self.feedback) > 10

    def __repr__(self):
        return '<User {0!r}>'.format(self.name)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    columns = db.relationship('Column', back_populates='category')

    def __repr__(self):
        return '<Category {0!r}>'.format(self.name)


class Column(db.Model):
    __tablename__ = 'columns'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', back_populates='columns')

    articles = db.relationship('Article', back_populates='column')

    def __repr__(self):
        return '<Column {0!r}>'.format(self.name)


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    text = db.Column(db.Text, nullable=False)
    feature = db.Column(db.PickleType, nullable=False)

    column_id = db.Column(db.Integer, db.ForeignKey('columns.id'), nullable=False)
    column = db.relationship('Column', back_populates='articles')

    def __repr__(self):
        return '<Article {0!r}>'.format(self.title)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), primary_key=True, nullable=False)
    opinion = db.Column(db.String, nullable=False)

    article = db.relationship('Article')


class Recommender(db.Model):
    __tablename__ = 'recommenders'
    recommender = db.Column(db.PickleType)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    user = db.relationship('User', back_populates='recommender')

    def __repr__(self):
        return '<Recommender for user_id={}>'.format(self.user_id)

    def fit(self):
        features = []
        opinions = []
        for feedback in self.user.feedback:
            features.append(feedback.article.feature)
            opinions.append(feedback.opinion)
        self.recommender = MultinomialNB().fit(features, opinions)

    def recommend(self, k):
        features = [article.feature for article in Article.query.all()]
        probs = self.recommender.predict_proba(features)
        like_idx, = np.where(self.recommender.classes_ == 'like')
        like_probs = probs[:, like_idx]
        article_ids = np.argpartition(like_probs, range(k))[:k]
        return Article.filter(Article.id.in_(article_ids)).all()