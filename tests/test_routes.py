def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Mars",
        "description": "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System",
        "diameter": 6787
    }

def test_no_planet_data_return_404(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_get_all_planets_return_valid_data(client,two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name":"Mars",
        "description": "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System",
        "diameter": 6787
        },
    {
        "id": 2,
        "name":"Venus",
        "description": "Venus is the second planet from the Sun. It is named after the Roman goddess of love and beauty",
        "diameter": 12104

    }]

def test_post_planet_data_return_201(client):
    # Act
    response = client.post("/planets",  json={
        "name":"Mars",
        "description": "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System",
        "diameter": 6787
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"
    
