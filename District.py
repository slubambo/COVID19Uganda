from decimal import Decimal

from pydantic import BaseModel, Field


class District:

    name: str = Field(..., alias="Country,Other")
    confirmed: int = Field(0, alias="TotalCases")
    deaths: int = Field(0, alias="TotalDeaths")
    hospitalizations: int = Field(0, alias="Hospitalizations")
