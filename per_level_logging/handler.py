from logging import Handler, LogRecord, NOTSET
from typing import Dict

class PerLevelHandler(Handler):
    def __init__(self, handlers: Dict[int, Handler]):
        Handler.__init__(self, NOTSET)
        self.handlers = handlers

    def emit(self, record: LogRecord):
        handler = self.handlers[record.levelno]
        if handler is not None:
            handler.emit(record)

    def flush(self):
        for handler in self.handlers.values():
            handler.flush()
