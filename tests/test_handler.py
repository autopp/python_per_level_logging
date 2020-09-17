from io import StringIO
import logging
import unittest
from unittest.mock import MagicMock

from per_level_logging import PerLevelHandler

class TestPerLevelHandler(unittest.TestCase):
    def setUp(self):
        self.info_warn_buf = StringIO()
        self.err_buf = StringIO()
        self.default_buf = StringIO()

        self.handlers = {
            logging.INFO: logging.StreamHandler(self.info_warn_buf),
            logging.WARNING: logging.StreamHandler(self.info_warn_buf),
            logging.ERROR: logging.StreamHandler(self.err_buf)
        }

    def test_output_to_shared_handler(self):
        handler, logger = self.create_handler_and_logger(self.handlers, None)
        logger.info("info message")
        logger.warning("warning message")

        self.assertEqual(self.info_warn_buf.getvalue(), "info message\nwarning message\n")
        self.assertEqual(self.err_buf.getvalue(), "")
        self.assertEqual(self.default_buf.getvalue(), "")
        handler.handleError.assert_not_called()

    def test_output_to_not_shared_handler(self):
        handler, logger = self.create_handler_and_logger(self.handlers, None)
        logger.error("error message")

        self.assertEqual(self.info_warn_buf.getvalue(), "")
        self.assertEqual(self.err_buf.getvalue(), "error message\n")
        self.assertEqual(self.default_buf.getvalue(), "")
        handler.handleError.assert_not_called()

    def test_output_to_not_set(self):
        handler, logger = self.create_handler_and_logger(self.handlers, None)
        logger.critical("critical message")

        self.assertEqual(self.info_warn_buf.getvalue(), "")
        self.assertEqual(self.err_buf.getvalue(), "")
        self.assertEqual(self.default_buf.getvalue(), "")
        handler.handleError.assert_not_called()

    def test_output_to_not_set_with_default(self):
        handler, logger = self.create_handler_and_logger(self.handlers, logging.StreamHandler(self.default_buf))
        logger.critical("critical message")

        self.assertEqual(self.info_warn_buf.getvalue(), "")
        self.assertEqual(self.err_buf.getvalue(), "")
        self.assertEqual(self.default_buf.getvalue(), "critical message\n")
        handler.handleError.assert_not_called()

    def test_flush(self):
        handler, _ = self.create_handler_and_logger(self.handlers, None)
        handler.flush()
        handler.handleError.assert_not_called()

    def create_handler_and_logger(self, handler, default):
        handler = PerLevelHandler(handlers, default)
        handler.handleError = MagicMock()
        logger = logging.getLogger('test')
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        return handler, logger
