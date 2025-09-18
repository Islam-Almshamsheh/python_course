import logging
logging.basicConfig(level=logging.DEBUG,
                    encoding="utf-8",
                    filename="my_logs.log",
                    filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s -[line: %(lineno)d - file name => %(filename)s] | logger name is %(name)s',
                    datefmt="%d/%B/%Y--%I:%M:%S_%p"  )
# Changingg the logger name instead of root:
# getlogger() => return logger with the specified name
my_logger = logging.getLogger("ISLAM_THE_BEST") 

# These functions log messages at different levels.
logging.debug("we are debugging")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
