import pytest
import tempfile
import os
from Project import allocation

from Project import database, users


@pytest.fixture(autouse=True)
def setup_test_database(monkeypatch):
    """
    Fresh temp database for EACH test.
    Avoids scope mismatch and Windows file locking.
    """

    db_fd, db_path = tempfile.mkstemp()
    os.close(db_fd)

    # Force all code to use this DB
    monkeypatch.setattr(database, "DATABASE_NAME", db_path)
    monkeypatch.setattr(users, "DATABASE_NAME", db_path)
   
    monkeypatch.setattr(allocation, "DATABASE_NAME", db_path)


    # Initialize schema + demo users
    database.init_database()
    users.init_users_table()
    users.setup_demo_users()

    yield

    try:
        os.remove(db_path)
    except PermissionError:
        pass
