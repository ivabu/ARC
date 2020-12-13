#!/usr/bin/python


#Student name: Iva Bubalo
#Email: i.bubalo1@nuigalway.ie
#Student ID: 20235871
#GitHub: https://github.com/ivabu/ARC/upload/master/src

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.



################################

#####Task 1: 6f8cd79b.json

#Required Transformation: Find the fist and last list in data, update the color of each element.
#Find first and last element in each list, update the color of the elements.

def solve_6f8cd79b(data):
    color = 8
    for i in range(0,len(data)): #update color for the first and last row
        if i == 0 or i == len(data)-1:
            for j in range(0,len(data[i])):
                data[i][j] = color
    for line in data: #update color for the fist and last element in each list
        line[0] = color
        line[-1] = color
    return data


#####Task 2: 3bd67248.json

#Required Transformation:
#Update the elements color of the last list.
#Start the iteration in the reversed order subtracting the iterator from the row length.

def solve_3bd67248(data):
    botttom_colour = 4
    diagonal_colour = 2
    # Bottom line colouring
    for i in range(0,len(data)):
        if i == len(data)-1:
            for j in range(1,len(data[i])):
                data[i][j] = bottom_colour

    # Diagonal line colouring
    i = len(data) - 1
    while i >= 0: #reversed iteration
        # If square not black, first list - 1 square at
        j = len(data[i]) - 1 #find current row length
        col = j - i #find current column, row lenght minus iterator
        if data[i][col] == 0: # black colour check
            data[i][col] = diagonal_colour 
        i = i - 1

    return data




#####Task 3: a2fd1cf0.json

#Required Transformation: Assign colours and find color coordinates. From red square we always draw horizontally,
#and from green square we always draw vertically until we meet the y coordinate of the red square.

def solve_a2fd1cf0(data):
    red = 2
    green = 3
    colour = 8
    red_coords = find_color_index(data, red)
    green_coords = find_color_index(data, green)

    if(red_coords[1] > green_coords[1]):
        # draw line to the left
        for i in range(green_coords[1], red_coords[1]):
            data[red_coords[0]][i] = colour
    else:
        for i in range(red_coords[1], green_coords[1]):
            data[red_coords[0]][i+1] = colour
        # draw in right direction
    if(red_coords[0] > green_coords[0]):
        for i in range(green_coords[0] + 1, red_coords[0]):
            data[i][green_coords[1]] = colour
        # draw upwards
    else:
        for i in range(red_coords[0], green_coords[0]):
            data[i][green_coords[1]] = colour
        # draw downwards

    return data

def find_color_index(data, colour):
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == colour:
                return i, j
            
############################


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

