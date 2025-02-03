from typing import Any, Type, Optional, TypeVar, List, Tuple
from collections import deque

# my code :3
# https://github.com/ellipticobj/perse-coding

def intinp() -> int:
    '''receives input as integer'''
    return int(input().strip())

def strinp() -> str:
    '''receives input as stripped string'''
    return input().strip()

def inp() -> str:
    '''receives input'''
    return input()

def linp(sep: Optional[str] = None, typec: Type = str) -> list:
    '''
    sep; separator
    typec: type converter
    '''
    return list(map(typec, input().split(sep)))

def splitstr(s: str, delim: str = " ") -> list[str]:
    '''splits a string at delim'''
    return s.split(delim)

def splitstrs(s: str, delims: List[str]) -> List[str]:
    '''splits strings using any delims'''
    import re
    pattern = f"[{re.escape(''.join(delims))}]"
    return re.split(pattern, s)

def revstr(s: str) -> str:
    '''reverses a string'''
    return s[::-1]

class Stack:
    '''last in first out'''
    def __init__(self) -> None:
        self.stack: List[Any] = []

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def pop(self) -> Optional[Any]:
        return self.stack.pop() if not self.isempty() else None

    def peek(self) -> Optional[Any]:
        return self.stack[-1] if not self.isempty() else None

    def isempty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)

class Queue:
    '''first in first out (optimized version)'''
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, item: Any) -> None:
        self.queue.append(item)

    def dequeue(self) -> Optional[Any]:
        return self.queue.popleft() if self.queue else None

    def front(self) -> Optional[Any]:
        return self.queue[0] if self.queue else None

    def isempty(self) -> bool:
        return len(self.queue) == 0

    def size(self) -> int:
        return len(self.queue)

def isprime(n: int) -> bool:
    '''checks if number is prime'''
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n%2 == 0 or n%3 == 0:
        return False

    i = 5
    while i**2 <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6

    return True

def sieve(n: int) -> List[int]:
    '''generates primes up to n using sieve of eratosthenes'''
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i : n+1 : i] = [False] * len(sieve[i*i : n+1 : i])

    return [i for i, val in enumerate(sieve) if val]

def factors(n: int) -> List[int]:
    '''returns factors of n'''
    if n == 0:
        return []

    factors = set()

    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            factors.add(i)
            factors.add(n//i)

    return sorted(factors)

def gcf(a: int, b: int) -> int:
    '''returns greatest common factor of a and b'''
    while b:
        a, b = b, a%b
    return a

def lcm(a: int, b: int) -> int:
    '''returns least common multiple of a and b'''
    return a*b//gcf(a, b)

T = TypeVar('T')
def perms(arr: List[T]) -> List[Tuple[T, ...]]:
    '''returns permutations of a list'''
    from itertools import permutations
    return list(permutations(arr))

def combs(arr: List[T], r: int) -> List[Tuple[T, ...]]:
    '''returns combinations of a list'''
    from itertools import combinations
    return list(combinations(arr, r))

def prettyprint(arr: List[Any], sep: str = "") -> None:
    '''pretty prints a list'''
    print(sep.join(map(str, arr)))

def ispalindrome(s: str) -> bool:
    '''checks if a string is palindrome'''
    return s == s[::-1]

def isanagram(s1: str, s2: str) -> bool:
    '''checks if two strings are anagrams'''
    return sorted(s1) == sorted(s2)

def compress(s: str) -> str:
    '''compresses a string'''
    compressed: List[str] = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1]+str(count))
            count = 1

    compressed.append(f"{s[-1]}{count if count > 1 else ''}")
    return "".join(compressed)

def longestcommonprefix(strs: List[str]) -> str:
    '''returns longest common prefix'''
    if not strs:
        return ""

    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]

def removedups(arr: List[Any]) -> List[Any]:
    '''
    removes duplicates from a list
    DOES NOT PRESERVE ORDER
    '''
    return list(set(arr))

def removedupsorder(arr: List[Any]) -> List[Any]:
    '''
    removes duplicates from a list
    PRESERVES ORDER
    '''
    seen = set()
    return [x for x in arr if not (x in seen or seen.add(x))]

def issubsequence(s: str, t: str) -> bool:
    '''checks if s is subsequence of t'''
    it = iter(t)
    return all(c in it for c in s)

def isrot(s1: str, s2: str) -> bool:
    '''checks if s2 is rotation of s1'''
    return len(s1) == len(s2) and s2 in s1 + s1

# !!
