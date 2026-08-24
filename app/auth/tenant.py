from app.auth.models import User
from app.core.exceptions import TenantIsolationError


def enforce_tenant(
    user: User,
    resource_tenant_id: str,
) -> None:

    if user.tenant_id != resource_tenant_id:
        raise TenantIsolationError(
            "Cross-tenant access denied"
        )


def tenant_filter(
    user: User,
) -> dict:

    return {
        "tenant_id": user.tenant_id
    }