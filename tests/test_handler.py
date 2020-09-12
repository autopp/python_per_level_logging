from io import StringIO
import logging
import unittest
from unittest.mock import MagicMock

from per_level_logging import PerLevelHandler

class TestPerLevelHandler(unittest.TestCase):
    def setUp(self):
        self.info_warn_buf = StringIO()
        self.err_buf = StringIO()
        self.handler = PerLevelHandler({
            logging.INFO: logging.StreamHandler(self.info_warn_buf),
            logging.WARNING: logging.StreamHandler(self.info_warn_buf),
            logging.ERROR: logging.StreamHandler(self.err_buf)
        })
        self.mockHandleError = MagicMock()
        self.handler.handleError = self.mockHandleError
        self.logger = logging.getLogger('test')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.handler)

    def test_output_to_shared_handler(self):
        self.logger.info("info message")
        self.logger.warning("warning message")

        self.assertEqual(self.info_warn_buf.getvalue(), "info message\nwarning message\n")
        self.assertEqual(self.err_buf.getvalue(), "")
        self.mockHandleError.assert_not_called()

    def test_output_to_not_shared_handler(self):
        self.logger.error("error message")

        self.assertEqual(self.info_warn_buf.getvalue(), "")
        self.assertEqual(self.err_buf.getvalue(), "error message\n")
        self.mockHandleError.assert_not_called()

    def test_output_to_not_set(self):
        self.logger.critical("critical message")

        self.assertEqual(self.info_warn_buf.getvalue(), "")
        self.assertEqual(self.err_buf.getvalue(), "")
        self.mockHandleError.assert_not_called()
