from pydantic import BaseModel
from wallet.PassProps.Alignment import Alignment


class FieldProps(BaseModel):
    key: str
    value: str
    label: str | None = None
    attributed_value: str | None = None
    change_message: str | None = None
    text_alignment: Alignment | str = Alignment.LEFT

    class Config:
        arbitrary_types_allowed = True
