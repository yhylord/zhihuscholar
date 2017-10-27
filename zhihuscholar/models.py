from zhihuscholar import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))

    feedback = db.relationship('Feedback')

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