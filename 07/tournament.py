from itertools import combinations
from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    StrategyError
)

def run_tournament(
    name: str, 
    roster_info: str, 
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(f"\n=== Tournament {name} ===")
    print(roster_info)
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for (fac1, strat1), (fac2, strat2) in combinations(opponents, 2):
            c1 = fac1.create_base()
            c2 = fac2.create_base()
            
            print("* Battle *")
            print(c1.describe())
            print("VS.")
            print(c2.describe())
            print("now fight!")
            
            strat1.act(c1)
            strat2.act(c2)
    except StrategyError as e:
        print(f"Battle error, aborting tournament: {e}")

if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()

    norm = NormalStrategy()
    defe = DefensiveStrategy()
    aggr = AggressiveStrategy()

    run_tournament(
        "0 (basic)", 
        "[ (Flameling+Normal), (Healing+Defensive) ]", 
        [(flame, norm), (heal, defe)]
    )

    run_tournament(
        "1 (error)", 
        "[ (Flameling+Aggressive), (Healing+Defensive) ]", 
        [(flame, aggr), (heal, defe)]
    )

    run_tournament(
        "2 (multiple)", 
        "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]", 
        [(aqua, norm), (heal, defe), (trans, aggr)]
    )
