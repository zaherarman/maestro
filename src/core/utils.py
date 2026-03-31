from models import TraceEvent
from typing import List

class TraceLogger:
    def __init__(self) -> None:
        self.events = []

    def log(self, operation_id: str, timestamp: float, event_type: str, message: str) -> None:
        self.events.append(
            TraceEvent(
                operation_id=operation_id,
                timestamp=timestamp,
                event_type=event_type,
                message=message,
            )
        )

    def get_operation_trace_via_id(self, operation_id: str) -> List[TraceEvent]:
        return [e for e in self.events if e.operation_id == operation_id]