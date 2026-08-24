class SecureAgentException(Exception):
    code = "secure_agent_error"
    status_code = 500

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class AuthenticationError(SecureAgentException):
    code = "authentication_failed"
    status_code = 401


class AuthorizationError(SecureAgentException):
    code = "authorization_denied"
    status_code = 403


class SecurityViolation(SecureAgentException):
    code = "security_violation"
    status_code = 400


class TenantIsolationError(AuthorizationError):
    code = "tenant_isolation_violation"


class ToolAuthorizationError(AuthorizationError):
    code = "tool_authorization_denied"


class InputSecurityError(SecurityViolation):
    code = "unsafe_input"


class OutputSecurityError(SecurityViolation):
    code = "unsafe_output"