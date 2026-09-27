from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator

class Rank(str, Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")
            
        has_commander_or_captain = any(
            c.rank in (Rank.commander, Rank.captain) for c in self.crew
        )
        if not has_commander_or_captain:
            raise ValueError("Mission must have at least one Commander or Captain")
            
        if not all(c.is_active for c in self.crew):
            raise ValueError("All crew members must be active")
            
        if self.duration_days > 365:
            experienced_count = sum(1 for c in self.crew if c.years_experience >= 5)
            if (experienced_count / len(self.crew)) < 0.5:
                raise ValueError("Long missions (> 365 days) need 50% experienced crew (5+ years)")
                
        return self

def main() -> None:
    print("=== Space Mission Crew Validation ===")
    
    member1 = CrewMember(
        member_id="C001", name="Sarah Connor", rank=Rank.commander, 
        age=45, specialization="Mission Command", years_experience=20
    )
    member2 = CrewMember(
        member_id="C002", name="John Smith", rank=Rank.lieutenant, 
        age=30, specialization="Navigation", years_experience=6
    )
    member3 = CrewMember(
        member_id="C003", name="Alice Johnson", rank=Rank.officer, 
        age=25, specialization="Engineering", years_experience=2
    )
    
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-12-01T08:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[member1, member2, member3]
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"Crew size: {len(valid_mission.crew)}")
        for c in valid_mission.crew:
            print(f"- {c.name} ({c.rank.value}): {c.specialization}")
        print()
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_VENUS",
            mission_name="Venus Flyby",
            destination="Venus",
            launch_date="2027-01-01T08:00:00",
            duration_days=100,
            budget_millions=500.0,
            crew=[member3]  # Błąd: brak komandora lub kapitana
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"- {error['msg']}")

if __name__ == "__main__":
    main()
