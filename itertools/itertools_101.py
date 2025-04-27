import itertools        

"""
Key Characteristics of Itertools Iterators
Lazy Evaluation: Iterators in itertools are evaluated lazily, meaning they generate items on-the-fly and do not store the entire sequence in memory.
Efficiency: This lazy evaluation makes itertools functions efficient for handling large datasets or infinite sequences.
Composability: Itertools iterators can be composed together to create complex data processing pipelines.
"""

def main ():
    for i in itertools.count(10):
        print(i)
        if(i == 15):
            break

    for i in itertools.repeat("Himangshu",3):
        print(i)

    for i in itertools.accumulate(range(1,11)):
        print(i)

    get_all_permutations()
    get_all_combinations()
    chaining_iterators()

    # Prints out numbers from 1 to 9, skipping even numbers
    print(list(itertools.filterfalse(lambda x:x%2==0, range(10))))

    # Starmap : Applies a function to each element of an iterable and returns an iterator that yields the results as a Iterable
    print(itertools.starmap(lambda x,y: x*y, [(2,3),(4,5),(6,7)]))

def get_all_combinations():
    items = ["a", "b", "c"]
    combinations = itertools.combinations(items, 2)
    print("All Combinations of length two:")
    print(list(combinations))
    
    print("\nCombinations with replacement:")
    combinations_with_replacement = itertools.combinations_with_replacement(items, 2)
    print(list(combinations_with_replacement))

def chaining_iterators() -> list:
    l1 = ["a", "b", "c"]
    l2 = ["d", "e"]

    print("Chaining Iterators: Find combinations of all elements in both lists with 2 selection:")
    print(list(itertools.combinations(itertools.chain(l1,l2), 2)))

def get_all_permutations() -> None:
    items = ["a", "b", "c"]
    perms = itertools.permutations(items)
    print("All Permutations:")
    for perm in perms:
        print(perm)

    print("\nPermutations of length two:")
    perms_of_length_two = itertools.permutations(items, 2)
    for perm in perms_of_length_two:
        print(perm)

if __name__ == "__main__":
    main()