#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 14:44:33 2023
Based on: https://www.kaggle.com/datasets/arbazmohammad/world-airports-and-airlines-datasets
Sample input: --AIRLINES="airlines.yaml" --AIRPORTS="airports.yaml" --ROUTES="routes.yaml" --QUESTION="q1" --GRAPH_TYPE="bar"
@author: rivera
@author: STUDENT_ID
"""

import pandas as pd
import argparse

# defining a function to get top songs that take sortBy, display, files as an input
def get_top_songs(sortBy, display, files):
    dfs = []  # Initialize an empty list to store the dataframes
    top_songs = pd.DataFrame()    # Initialize an empty dataframe for the top songs

    #Loop through each file in the input list
    for file in files:
        # Read the CSV file into a dataframe
        dataframe = pd.read_csv(file)
        
        # Sort the dataframe by the specified attribute (sortBy) and 'song' column in descending order
        sorted_df = dataframe.sort_values(by=[sortBy,'song'], ascending=[False,False])
        
        # Get the top 'display' number of songs from the sorted dataframe
        top_songs_ = sorted_df.head(display)
        
        # Append the top songs dataframe to the list
        dfs.append(top_songs_)
    
    # Concatenate all the dataframes in the list into a single dataframe
    combined_dataframe = pd.concat(dfs)
    
    # Select only the 'artist', 'song', 'year', and sortBy columns from the combined dataframe
    top_songs = combined_dataframe[['artist','song','year',sortBy]]
    
    # Sort the top songs dataframe by the specified attribute (sortBy) and 'song' column in descending order
    sorted_top_songs = top_songs.sort_values(by=[sortBy, 'song'], ascending=[False, False])
    
    # Return the top 'display' number of songs from the sorted top songs dataframe
    return sorted_top_songs.head(display)

def main():

    
 # Create an argument parser
    parser = argparse.ArgumentParser()
    
    # Add command-line arguments for 'sortBy', 'display', and 'files'
    parser.add_argument('--sortBy', type=str, choices=['popularity', 'energy', 'danceability'], default='popularity', help='Sort the songs by a specific attribute (popularity, energy, danceability)')
    parser.add_argument('--display', type=int, default=10, help='Number of songs to display')
    parser.add_argument('--files', type=str, help='List of input CSV files')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Extract the values of 'sortBy', 'display', and 'files' from the parsed arguments
    sort_by = args.sortBy
    display = args.display
    files = args.files.split(',')
    
    # Call the 'get_top_songs' function with the extracted values and store the result in 'top_songs'
    top_songs = get_top_songs(sort_by, display, files)
    
    # Save the 'top_songs' dataframe to a CSV file named 'output.csv' without the index column
    top_songs.to_csv('output.csv', index=False)

# Check if the current module is the main module
if __name__ == '__main__':
    # Call the 'main' function
    main()





