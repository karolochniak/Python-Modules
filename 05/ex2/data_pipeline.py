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


class ExportPlugin(typing.Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        lista: list[tuple[int, str]] = []
        for proc in self.processors:
            for _ in range(nb):
                if len(proc.kotek) > 0:
                    lista.append(proc.output())
        if(lista):
            plugin.process_output(lista)


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        strings : list[str] = []
        print("CSV Output:")
        for ranga, text in data:
            strings.append(text)
        wynik = ", ".join(strings)
        print(wynik)


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        stringi: list[str] = []
        for ranga, text in data:
            stringi.append(f'"item_{ranga}": "{text}"')
        wynik = ", ".join(stringi)
        print("{" + wynik + "}")


if __name__ == "__main__":
    print("=== Code Nexus Data Pipeline ===")
    
    print("Initialize Data Stream..")
    stream = DataStream()
    stream.print_processors_stats()
    
    print("Registering Processors")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    stream.register_processor(np)
    stream.register_processor(tp)
    stream.register_processor(lp)
    
    batch1 = [
        'Hello world', 
        [3.14, 1, 2.71], 
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 
        42, 
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()
    
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    # Tu wywołujemy nową metodę z Twojego Exercise 2!
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()
    
    batch2 = [
        21, 
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'], 
        [{'log_level': 'ERROR', 'log_message': '500 server crash'}, 
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}], 
        [32, 42, 64, 84, 128, 168], 
        'World hello'
    ]
    print("\nSend another batch of data:")
    stream.process_stream(batch2)
    stream.print_processors_stats()
    
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()