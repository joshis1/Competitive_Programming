# There's an algorithms tournament taking palce in which teams of programmers compete against 
# each other to solve algorithmic problems as fast as possible. teams compete in a round robin
# where each team faces off against all other teams. Only two teams compete against each other at a 
# time, and for each competition, one team is designated the home team, while the other team is the 
# away team. In each competition there's always one winner and one loser; there are no ties. A team 
# receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that
# receives the most amount of points.
# 
# Given an array of pairs representing the teams that have competed against each other and 
# and array containing the results of each competition, write a function that returns the winner 
# of the tournament. The input arrays are named competitions and resuls, respectively. The competitions 
# arrays has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 
# 30 character representing the name of the team. The result array contains information about the 
# winner of each corresponding competition in the competitions array. Specifically, results[i] denotes 
# the winner of competitions[i], where 1 in the results array means that the home team in the 
# corresponding competition won and a 0 means that the away team won. 
# It is guaranteed that exactly one team will win the tournament and that each team will compete against
# all other teams exactly once. It is also guaranteed that the tournament will always have at least 
# two teams.

# Sample Input 
# competitions = [ ["HTML", "C#"],
#                  ["C#", "Python"],
#                  ["Python", "HTML"] ]

#  results = [0,0,1]

# Sample Output
# "Python"
# C# beats HTML< Python beats C#, and Python beats HTML.
# HTML - 0 Points
# C# - 3 points
# Python - 6 points.


def tournamentWinner(competitions, results):
    # Write your code here.
    winner_dict = {}
    winner = None
    current_winner_total = 0
    for idx, result in enumerate(results):
       new_val = 0
       current_competitor = None
       if result == 0:
           if winner_dict.get(competitions[idx][1]) is None:
               new_val = 3
               winner_dict[competitions[idx][1]] = new_val
               current_competitor = competitions[idx][1]
           else:
                val = winner_dict.get(competitions[idx][1])
                new_val = val + 3
                winner_dict[competitions[idx][1]] = new_val
                current_competitor = competitions[idx][1]
       else:
           if winner_dict.get(competitions[idx][0]) is None:
               new_val = 3
               winner_dict[competitions[idx][0]] = new_val
               current_competitor = competitions[idx][0]
           else:
                val = winner_dict.get(competitions[idx][0])
                new_val = val + 3
                winner_dict[competitions[idx][0]] = new_val
                current_competitor = competitions[idx][0]

       if current_winner_total < new_val:
            current_winner_total = new_val
            winner = current_competitor

    return winner


if __name__ == '__main__':
    competitions = [ ["HTML", "C#"], ["C#", "Python"], ["Python", "C#"] ]
    results = [0, 0, 1]
    print(tournamentWinner(competitions, results))



            
           
