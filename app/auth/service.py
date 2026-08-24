import hashlib
import hmac

from app.auth.models import User


USERS = {
    "admin@example.com": {
        "password": "ChangeMe-Admin-123!",
        "user": User(
            id="user-admin",
            email="admin@example.com",
            tenant_id="tenant-a",
            roles=["admin", "analyst"],
        ),
    },
    "analyst@example.com": {
        "password": "ChangeMe-Analyst-123!",
        "user": User(
            id="user-analyst",
            email="analyst@example.com",
            tenant_id="tenant-a",
            roles=["analyst"],
        ),
    },
}


def _safe_compare(password: str, expected: str) -> bool:
    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    expected_hash = hashlib.sha256(
        expected.encode()
    ).hexdigest()

    return hmac.compare_digest(
        password_hash,
        expected_hash,
    )


def authenticate(email: str, password: str) -> User | None:
    record = USERS.get(email.lower())

    if not record:
        return None

    if not _safe_compare(
        password,
        record["password"],
    ):
        return None

    return record["user"]