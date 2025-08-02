from dataclasses import dataclass, field
from typing import List, Optional

from src.dom.node_type import NodeType

@dataclass
class Node:
    node_type: NodeType
    parent: Optional['Node'] = None
    children: List['Node'] = field(default_factory=list)
