// script.js
"use strict";

document.addEventListener("DOMContentLoaded", function() {
  let candidateCount = prompt("Enter the number of candidates:");
  let candidates = [];

  // Input candidates' names
  for (let i = 1; i <= candidateCount; i++) {
    let candidateName = prompt(`Enter the name for candidate ${i}:`);
    candidates.push({ name: candidateName, votes: 0 });
  }

  let voterCount = prompt("Enter the number of voters:");
  let votes = [];

  // Input votes
  for (let i = 1; i <= voterCount; i++) {
    let vote = prompt(`Voter ${i}, enter the name of the candidate you want to vote for (or press Enter for an empty vote):`);
    votes.push(vote);
  }

  // Count votes
  for (let vote of votes) {
    let candidate = candidates.find(c => c.name === vote);
    if (candidate) {
      candidate.votes++;
    }
  }

  // Find the winner
  let winner = candidates.reduce((prev, current) => (prev.votes > current.votes) ? prev : current);

  // Display results
  let resultsParagraph = document.getElementById('results');
  resultsParagraph.textContent = "Results:\n";
  for (let candidate of candidates) {
    resultsParagraph.textContent += `${candidate.name}: ${candidate.votes} votes\n`;
  }
  resultsParagraph.textContent += `Winner: ${winner.name} with ${winner.votes} votes`;
});
