# Itsy Bitsy URL

Similar to bit.ly and tinyurl - takes a long url as input and shortens it.
This is a dev project only using 3 unique characters to create shortened URL.
Hence the name Itsy Bitsy :-)


## Tech Stack
1. Python 3.7/Flask
1. SQLite3 database

### Want to use this project?

## Basics

1. Fork/Clone repo
1. Activate a virtualenv or pipenv
1. Install requirements from Pipfile
    pipenv shell
    pipenv install flask flask-sqlalchemy python-dotenv pytest

    It you don't have pipenv installed use one of the following commands:<br/>
        python3 -m pip install pipenv<br/>
        OR<br/>
        pip install pipenv<br/>

    Create sqlite3 database<br>
    pipenv shell<br>
    python3<br>
    >>> from url_shortener import create_app<br>
    >>> from url_shortener.extensions import db<br>
    >>> db.create_all(app=create_app())<br>
    >>> exit()


No warranties or expressed or implied.

## Future Additions

1. Create user accounts
2. Add visualizations to stats

## Contract Info

1. LinkedIn: https://www.linkedin.com/in/jess-brock/
1. https://jessicabrock.github.io
