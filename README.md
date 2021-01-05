# Advent of Code Letters

Some Advent of Code puzzles provide visual outputs which must be 
converted into text. This package is a helper to automate this task.

## Installation

```
pip install aoc_letters
```

## Usage

An example puzzle output may look something like

```python
word = [
    ['#', '#', '#', '#', ' ', '#', '#', '#', '#', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
    ['#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
    ['#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ']
]
```

When tidied and printed, this appears to be 
```
#### #### 
#    #    
###  ###  
#    #    
#    #    
#### #
```

This process can be automated through:

```python
import aoc_letters
parsed = aoc_letters.parse.word(word)
parsed
```

```python
'EF' 
```
