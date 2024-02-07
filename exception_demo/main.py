import base64
from dataclasses import dataclass
from typing import Union

@dataclass
class UriTooShortError(Exception):
    uri_data: bytes
    def __str__(self) -> str:
        return f"Uri data must be at least 2 but it was {len(self.uri_data)} "

@dataclass
class URI:
    scheme: str
    authority: str
    path: str
    query: str
    fragment: str

    def __str__(self) -> str:
        return (
            f"{self.scheme}://{self.authority}{self.path}?{self.query}#{self.fragment}"
        )


def to_uri(input_text: Union[str, int, bytes]) -> URI:
    if isinstance(input_text, str):
        input_text = input_text.encode()
    elif isinstance(input_text, int):
        input_text = str(input_text).encode()
    if len(input_text) < 2:
        raise UriTooShortError(input_text)
    return URI(
        scheme="data",
        authority="",
        path="",
        query=f"text/plain;cherset=us-ascii;base64,{base64.b64encode(input_text).decode()}",
        fragment="",
    )


def main() -> None:
   
    uri_data = input("enter data to encode: ")
    uri = to_uri(uri_data)
    print(uri)


if __name__ == "__main__":
    main()
