SNAKE = r"""  \
   \    __
    \  {oo}
       (__)\ 
         Y \\ 
           _\\__
          (_____)_
         (________)Oo*
"""

def bubble(message: str) -> str:
    bubble_length = len(message) + 2
    return f"""
 {"_" * bubble_length}
( {message} )
 {"-" * bubble_length}"""

def say(message: str) -> None:
    print(bubble(message))
    print(SNAKE)