import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List


@dataclass
class Expense:
    payer_id: str
    amount: float
    description: str
    group_id: str
    involved_users: List[str]
    expense_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    currency: str = "EGP"

    def to_dict(self) -> Dict:
        return {
            "_id": self.expense_id,
            "payer_id": self.payer_id,
            "amount": self.amount,
            "description": self.description,
            "group_id": self.group_id,
            "involved_users": self.involved_users,
            "timestamp": self.timestamp,
            "currency": self.currency,
        }

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            expense_id=data.get("_id"),
            payer_id=data.get("payer_id"),
            amount=data.get("amount"),
            description=data.get("description"),
            group_id=data.get("group_id"),
            involved_users=data.get("involved_users", []),
            timestamp=data.get("timestamp"),
            currency=data.get("currency"),
        )
