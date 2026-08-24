import logging
import sys


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
        stream=sys.stdout,
    )


audit_logger = logging.getLogger("secure_agent.audit")
security_logger = logging.getLogger("secure_agent.security")
app_logger = logging.getLogger("secure_agent.app")