from dataclasses import dataclass

@dataclass
class Example:
    name: str
    value: int = 0

@dataclass
class Product:
    product_id: str
    name: str
    routing: list[str]
    
@dataclass
class Machine:
    machine_id: str
    stage: str
    rate_per_hour: float
    supported_products: list[str]
    
@dataclass
class Order:
    order_id: str
    product_id: str
    quantity: int
    release_time: float
    due_time: float
    priority: int
    
@dataclass
class Operation:
    operation_id: str
    order_id: str
    stage: str
    product_id: str
    quantity: int
    predecessors: list[str]
    eligible_machines: list[str]
    processing_time: float
    material_requirements: dict[str, float]
    status: str="unscheduled"
    
@dataclass
class TraceEvent:
    operation_id: str
    timestamp: float
    event_type: str
    message: str

