import requests as r
import rich as rico
from rich.console import Console

resp = r.post("https://www.httpbin.org/post", 
              data={
                "key1": "value1",
                "key2": "a value with spaces and an apostrophe '",
                })



console = Console()
console.print(resp.json(), style="bold magenta")