from dataclasses import dataclass
from typing import Self

@dataclass
class NumberIterator:
    maxm: int # Note that: order matters here. Since we are using just NumberIterator(10) and num is default, dataclass will take this as maxm values
    num: int = 0

    def __iter__(self) -> Self:
        return self
    def __next__(self) -> int:
        if(self.num >= self.maxm):
            raise StopIteration
        else:
            self.num += 1
            return self.num

def main():
    for num in NumberIterator(10):
        print(num)

if __name__ == "__main__":
    main ()