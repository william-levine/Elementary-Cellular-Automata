# Elementary Cellular Automata

## About
This program allows you to generate any of the 256 [Elementary Cellular Automata](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html) by providing the corresponding Wolfram rule number.


## Prerequisites
`numpy` must be installed

## How to run
```python
python3 main.py [-s SIZE] [-g GENERATIONS]
``` 

### Arguments
All arguments are optional as there are default values for each. 

`--generations` or `-g`: The number of generations to run

- For example, `--generations=100`, or `-g=10`
- Default value is **50**
- A value of **-1** will cause the program to run until manually terminated (Ctrl+C)

`--size` or `-s`: The number of cells in the CA 
- For example, `--size=125`, or `-s=13`
- An odd value will allow for a middle cell for perfect symmetry (not necessary but may be desired)
- Default value is **71**
- Choosing a value that exceeds the terminal width will cause the program to default to the terminal width
