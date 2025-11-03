# Tomography.py Example Output

This document shows example outputs from running `tomography.py`.

## How to Run

```bash
python3 tomography.py
```

## What It Does

The script:
1. Generates a random 5x5 mineboard with 5 mines placed randomly
2. Calculates an xrayboard where each cell shows the count of mines visible from that position (through row, column, and diagonal lines)
3. Prints both boards

## Example Output 1

```
1 0 0 0 0  
0 1 0 0 0  
0 0 0 0 0  
0 0 1 0 1  
0 0 1 0 0  
 
5 3 4 1 2  
3 5 4 1 3  
3 2 4 2 2  
3 4 6 5 5  
2 3 5 3 4  
```

**First board (mineboard):** Shows positions of mines (1 = mine, 0 = empty)
**Second board (xrayboard):** Shows the count of mines visible from each position

## Example Output 2

```
0 0 0 0 0  
0 0 0 0 1  
0 0 0 1 1  
0 0 0 0 0  
0 0 0 1 1  
 
1 1 1 3 3  
2 2 2 4 7  
2 3 3 7 7  
0 0 3 4 5  
2 4 3 6 7  
```

## Interpretation

Each cell in the xrayboard counts how many mines (1s) can be "seen" from that position by looking:
- Horizontally (across the row)
- Vertically (down the column)
- Diagonally (both directions)

This represents a tomography problem where you need to deduce the positions of mines based on the "x-ray" counts from different angles.
