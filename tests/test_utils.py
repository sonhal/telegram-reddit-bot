from bot import utils
import pytest
from collections.abc import Mapping


def test_read_env__return_object():
    assert utils.read_env() is not None


def test_read_env__return_not_empty():
    res = utils.read_env()
    assert len(res) > 0


def test_read_env__return_mapping():
    res = utils.read_env()
    assert isinstance(res, Mapping)