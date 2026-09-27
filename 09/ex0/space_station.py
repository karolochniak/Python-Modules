from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)

def main() -> None:
    print("=== Space Station Data Validation ===")
    
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-09-26T10:00:00",
            is_operational=True
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {'Operational' if station.is_operational else 'Down'}\n")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Alpha Base",
            crew_size=25,  # Error: maks is 20
            power_level=105.0,  # Error: maks is 100.0
            oxygen_level=98.0,
            last_maintenance="2026-09-26T10:00:00"
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"- {error['loc'][0]}: {error['msg']}")

if __name__ == "__main__":
    main()
