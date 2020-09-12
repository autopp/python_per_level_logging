from logging import Handler, LogRecord, NOTSET
from typing import Dict, Optional

class PerLevelHandler(Handler):
    def __init__(self, handlers: Dict[int, Handler], default: Optional[Handler] = None):
        Handler.__init__(self, NOTSET)
        self.handlers = handlers
        self.default = default

    def emit(self, record: LogRecord):
        handler = self.handlers.get(record.levelno, None)
        if handler is not None:
            handler.emit(record)
        elif self.default is not None:
            self.default.emit(record)

    def flush(self):
        for handler in self.handlers.values():
            handler.flush()
        if self.default is not None:
            self.default.flush()
