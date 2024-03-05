from __future__ import annotations

from enum import Enum
import re
from typing import Annotated, Optional
from typing_extensions import Self
from pydantic import BaseModel, Field, HttpUrl, StringConstraints, model_validator


class Category(Enum):
    """Category options for a race"""

    ONE_DAY = "one-day"
    STAGE = "stage"
    MONUMENT = "monument"
    GRAND_TOUR = "grand-tour"


class Race(BaseModel):
    """Model for the UCI World Tour races"""

    class Config:
        """Configurations for the model"""

        extra = "forbid"

    name: str = Field(..., description="Known name of the race")
    country: str = Field(..., description="Country where race is held")
    category: Category = Field(..., description="Category of race")
    when: str = Field(
        ..., description="The approximate date that race usually takes place"
    )
    first_edition: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True, to_upper=True, pattern=r"^(18|19|20)\d{2}$"
        ),
    ] = Field(..., description="The year the race was held for the first time")
    distance: Optional[Annotated[float, Field(strict=True, ge=0.0, le=300.0)]] = Field(
        ..., description="The approximate distance of race if it's a one-day race"
    )
    is_classic: Optional[str] = Field(
        ..., description="If race is a classic, include the name of the classics"
    )
    also_known_as: Optional[list[str]] = Field(
        None, description="Other names or nicknames for the race"
    )
    insights: Optional[str] = Field(
        None,
        description="Fun or important, insightful information that is not merely textbook knowledge"
    )
    pcs_url: Optional[HttpUrl] = Field(
        None, description="URL for race on ProCyclingStats"
    )

    @model_validator(mode='after')
    def verify_square(self) -> Self:
        """Verify that the URL includes a word with the name"""
        name_words = re.findall(r'\w+', self.name.lower())
        last_part_of_url = str(self.pcs_url).rsplit('/', maxsplit=1)[-1].lower()
        if not any(word in last_part_of_url for word in name_words):
            raise ValueError(f"The URL '{self.pcs_url}' does not include any word from the race name '{self.name}'")

        return self
