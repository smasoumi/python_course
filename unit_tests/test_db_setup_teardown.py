cnn = None

def setup_module(module):
    # this is initial step before running unit tests
    global cnn
    # make a connection to db
    # cnn = db.connect('server')
    pass

def teardown_module(module):
    # this is final step after unit tests
    # cnn.close()
    pass

def test_db():
    assert True


