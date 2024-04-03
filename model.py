"""A Pydantic model to store variables"""

from typing import Dict, List
from pydantic import BaseModel, ValidationError


class ModelParameters(BaseModel):
    """PyDantic model to parse a dictionary from the json object
    """
    variables: Dict[str, List[int]]
