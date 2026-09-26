import typing
import abc

class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.kotek: list[tuple[int, str]] = []
        self.counter: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        return self.kotek.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self.kotek.append((self.counter, str(item)))
                self.counter += 1
        else:
            self.kotek.append((self.counter, str(data)))
            self.counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self.kotek.append((self.counter, item))
                self.counter += 1
        else:
            self.kotek.append((self.counter, data))
            self.counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        def is_valid_dict(d: typing.Any) -> bool:
            if not isinstance(d, dict):
                return False
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(isinstance(x, dict) and is_valid_dict(x) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            if "log_level" in d and "log_message" in d:
                return f"{d['log_level']}: {d['log_message']}"
            return ", ".join(f"{k}: {v}" for k, v in d.items())

        if isinstance(data, list):
            for item in data:
                self.kotek.append((self.counter, format_log(item)))
                self.counter += 1
        else:
            self.kotek.append((self.counter, format_log(data)))
            self.counter += 1


class DataStream():
    def __init__(self) -> None:
        self.processors : list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(f"DataStream error: Can't process element in stream: {element}")


    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if(self.processors == []):
            print("No processor found, no data")
        else:
            for proc in self.processors:
                name = proc.__class__.__name__.replace("Processor", " Processor")
                print(f"{name}: total {proc.counter} items processed \
                      remaining {len(proc.kotek)} on processor")

if __name__ == "__main__":
    print("=== Code Nexus Data Stream ===")
    
    print("Initialize Data Stream..")
    stream = DataStream()
    stream.print_processors_stats()
    
    print("Registering Numeric Processor")
    np = NumericProcessor()
    stream.register_processor(np)
    
    batch = [
        'Hello world', 
        [3.14, 1, 2.71], 
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ], 
        42, 
        ['Hi', 'five']
    ]
    
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    
    print("Registering other data processors \n")
    tp = TextProcessor()
    lp = LogProcessor()
    stream.register_processor(tp)
    stream.register_processor(lp)
    
    print("Send the same batch again \n")
    stream.process_stream(batch)
    stream.print_processors_stats()
    
    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    for _ in range(1):
        lp.output()
        
    stream.print_processors_stats()