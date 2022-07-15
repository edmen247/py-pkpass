from pydantic import BaseModel
from wallet.PassProps.Alignment import Alignment
from typing import Optional, Union


class FieldProps(BaseModel):
    key: str
    value: str
    label: Optional[str] = None
    attributed_value: Optional[str] = None
    change_message: Optional[str] = None
    text_alignment: Optional[Union[Alignment, str]] = Alignment.LEFT

    class Config:
        arbitrary_types_allowed = True
