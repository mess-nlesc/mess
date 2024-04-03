"""A Pydantic model to store variables"""

from typing import Dict, List
from pydantic import BaseModel, Field

class ParametersModel(BaseModel):
    """PyDantic model to parse a dictionary from the json object
    """
    variables: Dict[str, List[int]]
