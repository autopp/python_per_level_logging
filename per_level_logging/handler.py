#
# Copyright (C) 2020 Akira Tanimura
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from logging import Handler, LogRecord, NOTSET
from typing import Dict, Optional

class PerLevelHandler(Handler):
    def __init__(self, handlers: Dict[int, Handler], default: Optional[Handler] = None):
        Handler.__init__(self, NOTSET)
        self.handlers = handlers
        self.default = default

    def emit(self, record: LogRecord):
        handler = self.handlers.get(record.levelno, self.default)
        if handler is not None:
            handler.emit(record)

    def flush(self):
        for handler in self.handlers.values():
            handler.flush()
        if self.default is not None:
            self.default.flush()
