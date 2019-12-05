

def test_delete_first_subscriber(app):
    app.session.login(username="admin", password="secret")
    app.subscriber.delete_first_subscriber()
    app.session.logout()