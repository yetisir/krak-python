# coding: utf-8

"""
    Krak REST API

    Krak REST API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.borehole_input import BoreholeInput  # noqa: E501
from openapi_client.rest import ApiException

class TestBoreholeInput(unittest.TestCase):
    """BoreholeInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BoreholeInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.borehole_input.BoreholeInput()  # noqa: E501
        if include_optional :
            return BoreholeInput(
                name = '0', 
                easting = 1.337, 
                northing = 1.337, 
                elevation = 1.337
            )
        else :
            return BoreholeInput(
                name = '0',
                easting = 1.337,
                northing = 1.337,
                elevation = 1.337,
        )

    def testBoreholeInput(self):
        """Test BoreholeInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
