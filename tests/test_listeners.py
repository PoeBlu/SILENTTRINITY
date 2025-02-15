import pytest
import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from core.teamserver.loader import Loader
from core.teamserver.listener import Listener

@pytest.fixture
def listener_loader():
    ''' Load all of the listeners'''
    return Loader(type="listener", paths=["core/teamserver/listeners/"])

def test_listeners(listener_loader):
    for l in listener_loader.loaded:
        print(f"Testing listener '{l.name}'")
        assert isinstance(l, Listener)
