# per_level_logging

per_level_logging is implementation of `logging.Handler` to change the output per level.

## Install

```
$ pip install per_level_logging
```

## Usage

`per_level_logging.PerLevelHandler` implements `logging.Handler`. It receives the map from log level to actual handler.

```python
from logging import INFO, ERROR, StreamHandler, getLogger
import sys

from per_level_logging import PerLevelHandler

# initialize handler with info and error level handler
handler = PerLevelHandler({
    INFO: StreamHandler(sys.stdout),
    ERROR: StreamHandler(sys.stderr)
})

logger = getLogger('sample')
logger.addHandler(handler)

logger.info('info message') # output to stdout
logger.error('error message') # output to stderr
logger.debug('debug message') # not output anywhere!
```

You can pass the optional handler to default output

```python
from logging import INFO, ERROR, StreamHandler, getLogger
import sys

from per_level_logging import PerLevelHandler

# initialize handler with info and error level handler
handler = PerLevelHandler(
    {
      INFO: StreamHandler(sys.stdout),
      ERROR: StreamHandler(sys.stderr)
    },
    StreamHandler(sys.stderr) # handler for level which is not specified
)

logger = getLogger('sample')
logger.addHandler(handler)

logger.info('info message') # output to stdout
logger.error('error message') # output to stderr
logger.debug('debug message') # output to stderr (by default handler)
```

Internally, `PerLevelHandler.emit` delegates output to the correspond handler. `PerLevelHandler.flush` broadcasts all handlers.

## License

[Apache License 2.0](LICENSE)
