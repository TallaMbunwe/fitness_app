import pytest
from src.app import check_user_password


def test_index():
    #assert index() == "Hello, world!"
    ...

def home_page():
    with pytest.raises(ValueError):
        #home_page(follower)
        ...

#def test_check_user_password():
#    with pytest.raises(FileNotFoundError):
#        check_user_password("badboss","sdakojsjaaf")

def test_check_user_password():
        check_user_password("badboss","sdakojsjaaf") == "That file was not found Let me create it"

def test_get_user_credentials():
    #with pytest.raises()
    ...

def test_authentication():
    ...

def test_account_creation():
    ...

def test_login():
    ...

