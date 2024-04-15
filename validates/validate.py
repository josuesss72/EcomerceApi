from interfaces.db_interface import TRequestDocument
from typing import Literal, Union

TValidate = Union[TRequestDocument, Literal[False]]
