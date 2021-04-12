import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_true, assert_is_not_none, assert_list_equal, assert_dict_equal
from watchdough import UI, get_data

class TestUI(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_datan_latauspyynto_onnistuu(self):
        with patch('requests.get') as mock_get:
            # Configure the mock to return a response with an OK status code.
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = {'humidity': 61.775, 'temp': 23.699999999999992, 'distance': 12.936150000000001}

            # Call the service, which will send a request to the server.
            data = get_data("DEV")
            
        assert_is_not_none(data)
        assert_dict_equal(data, {'humidity': 61.775, 'temp': 23.699999999999992, 'distance': 12.936150000000001})