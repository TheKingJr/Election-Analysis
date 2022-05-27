#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:58:28 2022

@author: origi
"""

import csv
import os

#Assigning a variable for the file to load and the path
file_to_load = os.path.join("/Users/origi/Documents/Data Bootcamp/Challenge 3/election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("/Users/origi/Documents/Data Bootcamp/Challenge 3/Analysis/Analysis.txt")

    

#Initialize a total vote counter
total_votes = 0

#Candidate options - Used for 'if loop' to gather all the candidates
Candidate_options = []

#Counties - Used for 'if loop' to gather all the counties
Counties = []

#Creating an empty dictionary to hold candidates and their respective votes
candidate_votes = {}

#Creating another empty dictionary for counties and their respective participation
County_count = {}

#Creating an empty dictionary - to extract information from 'for loop' for printing
candidate_results = []

#Creating an empty dictionary - to extract information from 'for loop' for printing
county_results = []



#open the election results and read the file
with open(file_to_load) as Edata:
    
    # To do: read and analyze the data here
    
    # Read the file object with the reader function
    file_reader = csv.reader(Edata)
    
    #Print the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for i in file_reader:
        #Add to the total vote count
        total_votes +=1
        
        #Print the candidate name from each row
        candidate_name = i[2]
        
        #Print the county name from each row
        county_name = i[1]
        
        #If the candidate does not match any exisiting candidate
        if candidate_name not in Candidate_options:
        
            #Add the candidate anem to the candidate list
            Candidate_options.append(candidate_name)
            
            #Tracks a specific candidate's vote count
            candidate_votes[candidate_name] = 0
            
        #Adds a vote to that specific candidate's tally
        candidate_votes[candidate_name] +=1
        
        #If the county does not match any existing county
        if county_name not in Counties:
        
            #Add the county name to the county list
            Counties.append(county_name)
            
            #Tracks a specific voter's participation
            County_count[county_name] = 0
            
        #Adds one to that specific county's tally
        County_count[county_name] +=1
        
        
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
        
    # #Print the total votes - used for verification purposes
    # print(total_votes)
    
    # #Print the candidate list - used for verification purposes
    # print(Candidate_options)
    
    # #Print the candidate vote dictionary - used for verification purposes
    # print(candidate_votes)
        
    #Calculating voting percentage for each candidate by looping through the counts
    
    #Winning candidate and winning count tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    
    #Determining county participation and largest county turnover count tracker
    winning_county = ""
    wcc = 0 #winning county count
    wcp = 0 #winning county percentage
    
    
    #Iterating thorugh the candidate list
    for candidate_name in candidate_votes:
        
        #Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        
        #Calculating the percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
    
        
        
        #Task: find the winner - candidate's name, vote count, and percentage of votes to the terminal
        
        #Determining the winning vote count and candidate - if votes is greater than winning count
        if (votes>winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            
            winning_percentage = vote_percentage
            
            #setting the winning_candidate equal to the candidates name
            winning_candidate = candidate_name
            
        #Task: print out ecah candidate's name, vote count, and percentage of votes to terminal
        
        #Appending the results so that I can print them out later
        candidate_results.append(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
    #Iterating thorugh the county list to determine largest voter turnout
    for county_name in County_count:
        
        #Retrieve vote count of county
        turnover = County_count[county_name]
        
        #Calculating the percentage of voters
        turnover_percentage = float(turnover)/float(total_votes)*100
    
        
        
        #Task: find the winner - county's name, voter turnout, and percentage of voters to the terminal
        
        #Determining the winning vote count and candidate - if votes is greater than winning count
        if (turnover>wcc) and (turnover_percentage > wcp):
            #If true then set winning_county_count (wcc) = votes and winning_county_percentage (wcp) = vote percentage
            wcc = turnover
            
            wcp = turnover_percentage
            
            #setting the winning_county equal to the county name
            winning_county = county_name
            
        #Task 1: print out ecah candidate's name, vote count, and percentage of votes to terminal
        #Task 2: print out ecah countie name, vote count, and percentage of votes to terminal
        
        #Appending the results so that I can print them out later
        county_results.append(f"{county_name}: {turnover_percentage:.1f}% ({turnover:,})\n")
       
     
       
    #Printing out election results in summary format for candidates and counties    
    winning_candidate_summary = (
        
        f"-------------------------\n"
        
        f"Winner: {winning_candidate}\n"
        
        f"Winning Vote Count: {winning_count:,}\n"
        
        f"Winning percentage: {winning_percentage:.1f}%\n"
        
        f"-------------------------\n"
        
        
        )
    
        
    winning_county_summary = (
        
        f"\nCounty Votes:\n"
        
        f"\n{county_results[0]} \n"
        
        f"\n{county_results[1]}\n"
        
        f"\n{county_results[2]}\n"
        
        f"\n-------------------------\n"
        
        f"Largest County Turnout: {winning_county}\n"
        
        f"-------------------------\n"
        
        )
    
 

    #Print the final vote count to the terminal
    election_results = (
        
        f"\nElection Results \n"
        
        f"\n-------------------------\n"
        
        f"Total Votes: {total_votes:,}\n"
        
        
        f"\n-------------------------\n"
        )
    
    #Formatting the candidate results for terminal output
    candidate_results_final = (
        
        f"\n{candidate_results[0]} \n"
        
        f"\n{candidate_results[1]}\n"
        
        f"\n{candidate_results[2]}\n"
        
        f"-------------------------"
        
        )
    
    #Print the total votes
    print(election_results, end="")
    
    #Print each candidate, their voter count, and percentage to the terminal
    print(candidate_results)
    
    #Print the winner
    print(winning_candidate_summary)
    
    #Print the winning county summary
    print(winning_county_summary)
    
    
    #Save the final vote to the text file.
    txt_file.write(election_results)
    
    #Save the county results to the text file.
    txt_file.write(winning_county_summary)
    
    #Save the candidate results to the text file.
    txt_file.write(candidate_results_final)
    
    #Save the winning summmary to the text file.
    txt_file.write(winning_candidate_summary)
    

