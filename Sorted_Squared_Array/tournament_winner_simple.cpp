#include <vector>
#include <iostream>
#include <map>
#include <array>

using namespace std;

void updateScores(string winningTeam, int points, map<string, int> &scores)
{
     if(scores.find(winningTeam) == scores.end())
     {
        scores[winningTeam] = 0;   
     }
     
     scores[winningTeam] += points;

}

string tournamentWinner(vector<vector<string>> competitions,
                        vector<int> results)
{

   string best_Team = "";
   map<string, int> scores = {{best_Team, 0}};

    for(int idx = 0; idx < competitions.size(); idx ++)
    {
        auto competition = competitions[idx];
        // structural binding - works with fixed size only
        // so it cannot work with vector, need to convert to
        auto [homeTeam, awayTeam] = array<string, 2>({competition[0], competition[1]});
         //auto homeTeam = competition[0];
        //auto awayTeam = competition[1];
        auto result = results[idx];

        string winningTeam = result == 1 ? homeTeam : awayTeam;

        updateScores(winningTeam, 3, scores);

        if( scores[winningTeam] > scores[best_Team] )
        {
            best_Team = winningTeam;
        }

    }
    return best_Team;
}

int main()
{
    vector<vector<string>> competitions{{"HTML", "C#"}, {"C#", "Python"}, {"Python", "C#"}};
    vector<int> results{0, 0, 1};
    string winner = tournamentWinner(competitions, results);
    cout << winner.c_str();
    return 0;
}
