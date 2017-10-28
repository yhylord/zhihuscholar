from setuptools import setup


setup(
    name='zhihuscholar',
    version='0.1dev',
    packages=['zhihuscholar'],
    include_package_data=True,
    install_requires=[
        'alembic',
        'flask',
        'flask-bcrypt',
        'flask-login',
        'flask-sqlalchemy',
        'flask-wtf',
        'scikit-learn',
    ],
    python_requires='>=3',
)
