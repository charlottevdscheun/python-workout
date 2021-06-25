from typing import Iterator, List

class MagicIter:
    def __init__(self, max_list, total):
        self.max_list = max_list
        self.total = total
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):   
        if self.index >= len(self.max_list):
            raise StopIteration
        value = self.max_list[self.index]
        self.index += 1
        x = self.total - value
        return (value, x)


def magic_tuple(total: int, max:int) -> Iterator:
    """
    Parameters
    ----------
    total : int
        the total to which each tuple should sum.
    max:    int
        One more than the maximum number that can appear in any tuple.

    Returns
    -------
    out : List
        Magic list of tuples
    """
    max_list  = list(range(total-(max-1), max))
    magic_tuple_list = MagicIter(max_list, total)

    return magic_tuple_list


for t in magic_tuple(5,4):
        print(t)