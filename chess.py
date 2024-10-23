from players import players
from match import match
from typing import List, Tuple, Callable, Any

def name(per: Tuple[str, str, int, str,int]) -> str:
    return per[0]
def fed(per: Tuple[str, str, int, str,int]) -> str:
    return per[1]
def rate(per: Tuple[str, str, int, str,int]) -> int:
    return per[2]
def title(per: Tuple[str, str, int, str,int]) -> str:
    return per[3]
def year(per: Tuple[str, str, int, str,int]) -> int:
    return per[4]

def whatname(que: str) -> str:
    for x in players:
        if name(x)==que:
            if rate(x)<2000:
                return "Bad Player Found"
            return "Player Found"
    "Player Not Found"
def fedName(que: str) -> str:
    for x in players:
        if name(x)==que:
            return fed(x)
    return "Player is not found"
def rateName(que:str) -> int:
    for x in players:
         if name(x)==que:
             return rate(x)
    return "Player is not found"
def titleName(que:str) -> str:
    for x in players:
        if name(x)==que:
            return title(x)
    return "Player Not Found"

def yearName(que:str) -> int:
    for x in players:
        if name(x)==que:
            return year(x)
    return "Player Not Found"



pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("% was born in what _"), yearName),
    (str.split("what federation is %"), fedName),
    (str.split("what _ is %"), rateName),
    (str.split("% 's title"), titleName),
]


def search_pa_list(src:str) -> str:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    pass
    
    for pat, act in pa_list:
        val=match(pat,src)
        print(val)
        if val!=None:
            
            if act(val)!=None:
                return act(val)
            return ["No answers"]
    return ["I don't understand"]
         
        


assert fedName("MagnusCarlsen")=="Norway","Wrong"
assert whatname("MagnusCarlsen")== "Player Found", "Wrong"
assert rateName("MagnusCarlsen")== 2831,"Wrong"
assert titleName("MagnusCarlsen")== "Grandmaster","Wrong"
assert yearName("MagnusCarlsen")==1990,"Wrong"
assert search_pa_list("MagnusCarlsen was born in what year")==1990,"Wrong"
print("Done")