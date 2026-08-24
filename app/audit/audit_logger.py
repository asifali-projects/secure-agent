import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger(
    "secure_agent.security_audit"
)


def audit_event(
    *,
    event: str,
    user_id: str | None,
    tenant_id: str | None,
    request_id: str | None,
    metadata: dict | None = None,
):

    record = {
        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),

        "event": event,
        "user_id": user_id,
        "tenant_id": tenant_id,
        "request_id": request_id,
        "metadata": metadata or {},
    }

    logger.info(
        json.dumps(record)
    )