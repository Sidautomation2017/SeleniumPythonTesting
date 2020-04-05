import pytest

from PyTestDemo.BaseClass import Base


@pytest.mark.usefixtures("setup")
class TestExample(Base):
    def test_first(self):
        log = self.getLogger(__name__)
        log.info("I am in first method")
        print("I am in first method")

    def test_second(self):
        print("I am in second test")

    def test_dataFromFixture(self, dataLoad):
        log = self.getLogger(__name__)
        log.info(dataLoad)
        print(dataLoad)
