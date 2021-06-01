import logging
import sys


# Default Log Handler
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
log_handler.setLevel(logging.INFO)

# Velocloud Log Handler
vc_log_handler = logging.StreamHandler(sys.stdout)
vc_log_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s'))
vc_log_handler.setLevel(logging.INFO)


# Loggers
root_logger = logging.getLogger()
root_logger.propagate = False
root_logger.addHandler(log_handler)
root_logger.setLevel(logging.INFO)

vc_logger = logging.getLogger(__name__)
vc_logger.propagate = False
vc_logger.addHandler(vc_log_handler)
vc_logger.setLevel(logging.INFO)
