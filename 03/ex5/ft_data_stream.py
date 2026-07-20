import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'use',
               'release']
    while True:
        # yield pauzuje funkcję i zwraca wylosowaną krotkę
        yield (random.choice(players), random.choice(actions))


def consume_event(event_list: list[tuple[str, str]]) -> typing.Generator[
                              tuple[str, str], None, None]:
    while len(event_list) > 0:
        # Losujemy indeks i usuwamy element z listy
        idx = random.randint(0, len(event_list) - 1)
        event = event_list.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_events = []
    for _ in range(10):
        ten_events.append(next(stream))
    print(f"Built list of 10 events: {ten_events}")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
