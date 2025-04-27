from dataclasses import dataclass
"""
    Automatic Method Generation:
        Generates __init__(), __repr__(), __eq__(), etc., automatically.
    
    Type Annotations:
        Uses type annotations to define class fields.

    Default Values:
        Supports default values and default_factory for fields.
    
    Immutability:
        Can create immutable instances with frozen=True.
    
    Field Customization:
        Use field() for detailed field customization.
"""

from typing import Iterable
@dataclass
class LineItem:
    price: int
    quantity: int

    def total_price(self) -> int:
        return self.price * self.quantity
    
    def __hash__(self):
            return hash((self.price, self.quantity))
    
def print_totals(items: Iterable[LineItem]):
    for item in items:
        print(item.total_price())

def main() -> None:
    print("Iterators provide abstracton")
    
    print("Line items as List")
    line_item_list = [
        LineItem(10, 2),
        LineItem(5, 3)
    ]
    print_totals(line_item_list)
    
    print("Line items as Tuple")
    line_item_tuple = (
        LineItem(10, 2),
        LineItem(5, 3)
    )
    print_totals(line_item_tuple)

    print("Line items as Set")
    line_items_set = {
        LineItem(10, 2),
        LineItem(5, 3)
    }
    print_totals(line_items_set)

    """
    What happens if we remove the frozen=True?
    line_items_set will fail because it is not hashable anymore!

    How can we solve this ?
    We can use a custom hash function or make the class mutable again by removing frozen=True.
    Example     
    @dataclass(frozen=False)
    class LineItem:
        ... 
        def __hash__(self):
            return hash((self.price, self.quantity))
    """

main()