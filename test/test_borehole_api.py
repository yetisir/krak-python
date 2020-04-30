# coding: utf-8

"""
    Krak REST API

    Krak REST API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.borehole_api import BoreholeApi  # noqa: E501
from openapi_client.rest import ApiException


class TestBoreholeApi(unittest.TestCase):
    """BoreholeApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.borehole_api.BoreholeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_borehole_create(self):
        """Test case for borehole_create

        Create a new borehole  # noqa: E501
        """
        pass

    def test_borehole_delete(self):
        """Test case for borehole_delete

        Delete a borehole  # noqa: E501
        """
        pass

    def test_borehole_read_all(self):
        """Test case for borehole_read_all

        Read all boreholes in db, sorted by id  # noqa: E501
        """
        pass

    def test_borehole_read_one(self):
        """Test case for borehole_read_one

        Read one borehole  # noqa: E501
        """
        pass

    def test_borehole_update(self):
        """Test case for borehole_update

        Update a borehole  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
