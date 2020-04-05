import time

import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.TestData import TestData


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger(__name__)
        log.info("Test is started")
        homepage = HomePage(self.driver)
        homepage.form_Submission(getData["Name"], getData["Email"], getData["Gender"])
        time.sleep(3)
        log.info("Test is completed with name" + getData["Name"])

    @pytest.fixture(params=TestData.getTestData())
    def getData(self, request):
        return request.param
