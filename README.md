# election_analysis
Election Analysis using Python

## Project Overview
A Colorado Board of Elections employee has given me the task to copmlete the election audit of a recent local congressional election.

We had to:
1. Determine the total number of votes cast
2. Determine the candidates for the election
3. Calculate how many votes each candidate received
4. Calculate the percentage of votes each candidate received
5. Determine the winner of the election based on a popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    Charles Casper Stockham
    Diana DeGette
    Raymon Anthony Doane
- The results were:
    Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
    Diana Degette received 73.8% of the votes and 272,892 number of votes.
    Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
- The winner of the election was:
    Diana Degette who received 73.8% of the votes and 272,892 number of votes.

## Challenge Overview
The Colorado Board of Elections employee additionally requested that include some additional data to complete the audtio.

We had to:
1. Determine the list of each county represented in the voting data
2. Determine how many votes came from each county
3. Calculate the percentage of votes from each county
4. Determine the county with the highest turn out

## Challenge Summary
The analysis of the county data shows that:
- There were 3 candidates represented in the election. The 3 were:
    Jefferson
    Denver
    Arapahoe
- The results were:
    Jefferson had 10.5% of voters and 38,855 number of votes.
    Denver had 82.8% of voters and 306,055 number of votes.
    Jefferson had 6.7% of voters and 24,801 number of votes.
- The largest county was:
    Denver which had 82.8% of voters and 306,055 number of votes.

## Overall Summary
This program has the ability to read any election data that is in a similar format and determine both the election data for candidates, regardless of who runs or how many candidates run. It also has the ability to determine the statistics of the counties that were represented in the election. 

## Modifications
- One limitation of this program is in the data feed. If the data is written in a different format, it would not be read properly. Therefore, one modification that may need to be done is to ensure that (a) the county and candidates are either in the proper column in the csv or (b) the values for row[#] in line 50 and 53 are modified to the appropriate columns.
- Another modification that may be performed is to include census data to have more statistical data on the turn out of voters. Right now, Denver may have the largest count of voters but it could be that Denver just has a larger population. We could modify the code to factor the population of eligible voters to see if there is any information on what percentage of eligible voters are actually voting. We can then use that data to see if a larger push for voting may be needed.