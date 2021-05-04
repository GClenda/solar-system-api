import pytest
from app import create_app
from app import db

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

from app.models.planet import Planet

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mars_planet = Planet(name="Mars",
                      description= "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System",
                      diameter=6787)
    venus_planet = Planet(name="Venus",
                         description="Venus is the second planet from the Sun. It is named after the Roman goddess of love and beauty",
                         diameter=12104)

    db.session.add_all([mars_planet, venus_planet])
    
    db.session.commit()