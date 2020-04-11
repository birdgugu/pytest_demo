import sys
import pytest
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


class TestClsMark(object):
    @pytest.mark.debug
    def test_1(self):
        logging.info("ok")

    def test_2(self):
        logging.info("okk")

    @pytest.mark.level1
    def test_3(self):
        logging.info("I'm level1")
