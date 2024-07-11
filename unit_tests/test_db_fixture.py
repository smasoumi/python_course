# Fixtures leverage s concept of dependency injection
import pytest

# fixture is preferred over the setup-teardown approach
# by scope, we are sure that this function runs only once not more, like setup_module(module)
@pytest.fixture(scope="module")
def db_connection():
    cnn = None
    # make a connection to db and return the corresponding object
    # ...
    print('connecting to the database ...')
    yield cnn
    print('closing connection to the database.')
    # cnn.close() uncomment this when you implemented your own connection class


# kind of dependency injection
# test_db_connection has dependency on db_connection
def test_db_connection(db_connection):
    print('test db connection ...')
    assert True  # db_connection is not None


def test_db_command(db_connection):
    print('test db command ...')
    assert True  # run a command and check its effect on DB
