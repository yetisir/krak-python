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
from openapi_client.models.core_photo_input_crop_corners import CorePhotoInputCropCorners  # noqa: E501
from openapi_client.rest import ApiException

class TestCorePhotoInputCropCorners(unittest.TestCase):
    """CorePhotoInputCropCorners unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CorePhotoInputCropCorners
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.core_photo_input_crop_corners.CorePhotoInputCropCorners()  # noqa: E501
        if include_optional :
            return CorePhotoInputCropCorners(
                left = 1.337, 
                top = 1.337
            )
        else :
            return CorePhotoInputCropCorners(
        )

    def testCorePhotoInputCropCorners(self):
        """Test CorePhotoInputCropCorners"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
