import api

# todo check bad auth cases as separate test cases


def test_crud():
    api.login("admin", "admin123")

    data = {
        'name': "bob",
        'age': 39,
    }

    print('CREATE')

    resp = api.post('/api/data/user', data)

    id = resp['uid']

    data = {
        'name': "joe",
        'age': 40,
    }

    resp = api.post('/api/data/user', data)
    id2 = resp['uid']

    print('GET LIST')

    resp = api.get('/api/data/user/list')

    print('GET BY ID')

    resp = api.get('/api/data/user/' + id)

    print('QUERY')

    query = """{
  data(func: eq(name, "bob")) @filter(has(_user)) {
    uid
    name
    age
  }
}"""
    resp = api.post('/api/query', query, raw=True)

    print('UPDATE')

    data = {
        'name': 'rob',
        'age': 42,
    }

    resp = api.put("/api/data/user/" + id, data)

    print('GET BY ID')

    resp = api.get('/api/data/user/' + id)

    print('DELETE')

    api.delete('/api/data/user/' + id)
    api.delete('/api/data/user/' + id2)
