from typing import Any, Dict, Iterator, Optional

TDocument = Dict[str, Any]
TRequestDocument = Optional[TDocument]
TRequestDocumentAll = Iterator[TDocument]
