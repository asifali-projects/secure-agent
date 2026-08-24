from dataclasses import dataclass

from app.auth.models import User
from app.auth.rbac import has_role


@dataclass
class PolicyDecision:
    allowed: bool
    reason: str
    risk_score: int


class PolicyEngine:

    def evaluate_agent_request(
        self,
        user: User,
        intent: str,
        risk_score: int,
    ) -> PolicyDecision:

        if risk_score >= 90:

            if not has_role(user, "admin"):
                return PolicyDecision(
                    allowed=False,
                    reason="High-risk action requires admin",
                    risk_score=risk_score,
                )

        if intent == "privileged_operation":

            if not has_role(user, "admin"):
                return PolicyDecision(
                    allowed=False,
                    reason="Privileged operation denied",
                    risk_score=risk_score,
                )

        return PolicyDecision(
            allowed=True,
            reason="Policy allowed",
            risk_score=risk_score,
        )