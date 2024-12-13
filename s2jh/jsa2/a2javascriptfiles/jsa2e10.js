function startVoting() {
    const numCandidates = parseInt(prompt("Insert the number of candidates:"));
    const candidates = [];
    for (let i = 0; i < numCandidates; i++) {
      const name = prompt(`Insert the name for candidate ${i + 1}:`);
      candidates.push({ name: name, votes: 0 });
    }
    const numVoters = parseInt(prompt("Insert the number of voters:"));
    for (let i = 0; i < numVoters; i++) {
      const vote = prompt(`Voter ${i + 1}: Who do you vote for? (press enter if you don't want to vote):`);
      if (vote === "") {
        continue;
      }
      const candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());
      if (candidate) {
        candidate.votes++;
      } else {
        alert("Invalid candidate name. Please try again.");
        i--;
      }
    }
    candidates.sort((a, b) => b.votes - a.votes);
    const winner = candidates[0];
    let resultsList = `The winner is ${winner.name} with ${winner.votes} votes.\n\nResults:\n`;
    candidates.forEach(candidate => {
      resultsList += `${candidate.name}: ${candidate.votes} votes\n`;
    });
    document.getElementById("voteresult").innerText = resultsList;
  }
  startVoting();