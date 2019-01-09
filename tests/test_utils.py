from bot import utils
import pytest


def test_read_env__return_object():
    assert utils.read_env() is not None


def test_read_env__return_not_empty():
    res = utils.read_env()
    assert len(res) > 0
