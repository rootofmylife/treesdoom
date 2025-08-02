from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Element:
    tag_name: str
    attributes: Dict[str, str] = field(default_factory=dict)
