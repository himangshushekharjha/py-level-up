# Python Itertools

## What is an Iterator?
Object used to traverse through some sequence of objects

An iterator in Python is an object that implements the iterator protocol, which consists of the methods `__iter__()` and `__next__()`. Iterators are used to represent a stream of data that can be processed one element at a time.

Key characteristics of iterators:
- They allow sequential access to elements without loading the entire collection into memory
- They maintain their internal state, remembering where they are in the sequence
- They raise a `StopIteration` exception when there are no more elements to return
- They can only go forward (not backward) through the data
- They can be finite or infinite

Python's built-in functions like `iter()` and `next()` work with iterators, and many language constructs like for loops, list comprehensions, and generator expressions use iterators behind the scenes.

## Iterable vs Iterator
An Iteratable is an object that can provide you with an iterator
An Iterator is an object that allows you to iterate over it, and has a next() method that returns the next item in the sequence.