from pydantic import BaseModel, ConfigDict


class BaseModelDTO(BaseModel):
    model_config = ConfigDict(extra="forbid", use_enum_values=True)
