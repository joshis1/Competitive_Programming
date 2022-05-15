
function tournamentWinner(competitions, results) {
    let currentBestTeam = "";
    const scores  = { [currentBestTeam] : 0};
      
    for(let idx = 0; idx < competitions.length; idx++)
    {

        const result = results[idx];
        const [homeTeam, AwayTeam] = competitions[idx];
        const winningTeam = result === 1 ? homeTeam : AwayTeam;
        score_update(winningTeam, 3, scores);

        if( scores[winningTeam] > scores[currentBestTeam]) {
            currentBestTeam = winningTeam;
        }
        
    }

    return currentBestTeam;

  }

  function score_update(winningTeam, points, scores)
{
    if( !(winningTeam in scores)) {
        scores[winningTeam] = 0;
    }

    scores[winningTeam] += points;
}
  

competitions = [ ["HTML", "C#"], ["C#", "Python"], ["Python", "C#"] ];
results = [0, 0, 1];
console.log(tournamentWinner(competitions, results));
