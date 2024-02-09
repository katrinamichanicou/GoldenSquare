from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_cat_facts_provide():
    requester_mock = Mock(name="request")
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "fact":"All cats have claws, and all except the cheetah sheath them when at rest.",
        "length":73
        }

    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: All cats have claws, and all except the cheetah sheath them when at rest."
