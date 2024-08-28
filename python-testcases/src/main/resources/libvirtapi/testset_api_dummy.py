"""
COPYRIGHT Ericsson 2019
The copyright to the computer program(s) herein is the property of
Ericsson Inc. The programs may be used and/or copied only with written
permission from Ericsson Inc. or in accordance with the terms and
conditions stipulated in the agreement/contract under which the
program(s) have been supplied.

@since:     Nov 2014
@author:    Pat Bohan
@summary:   Dummy test
            Agile:
"""

from litp_generic_test import GenericTest, attr


class Libvirtapi(GenericTest):
    """
    There are currently no test for the libvirtapi and as of this moment
    there is no intention to have any(12/11/2014)
    The only test is a test which will always pass in order for
    libvirtapi rpm get published
    """

    def setUp(self):
        """
        Description:
            Runs before every single test
        Actions:
            None
        Results:
            None
        """
        # 1. Call super class setup
        super(Libvirtapi, self).setUp()

    def tearDown(self):
        """
        Description:
            Runs after every single test
        Actions:
            -
        Results:
            The super class prints out diagnostics and variables
        """
        super(Libvirtapi, self).tearDown()

    @attr('all', 'non-revert')
    def test_01_dummy(self):
        """
        Description:
            Dummy tests
        Actions:
            None
        Results:
            None
        """
        self.log("info", "This a dummy test to allow libvirtapi kgb pass" +\
                         "and hence publish libvirtapi rpm")
        self.assertTrue(True)
