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
from openapi_client.models.core_photo_input import CorePhotoInput  # noqa: E501
from openapi_client.rest import ApiException

class TestCorePhotoInput(unittest.TestCase):
    """CorePhotoInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CorePhotoInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.core_photo_input.CorePhotoInput()  # noqa: E501
        if include_optional :
            return CorePhotoInput(
                photo = bytes(b'blah'), 
                borehole_id = 56, 
                depth_from = 1.337, 
                depth_to = 1.337, 
                crop_corners = [
                    openapi_client.models.core_photo_input_crop_corners.core_photo_input_crop_corners(
                        left = 1.337, 
                        top = 1.337, )
                    ]
            )
        else :
            return CorePhotoInput(
        )

    def testCorePhotoInput(self):
        """Test CorePhotoInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
