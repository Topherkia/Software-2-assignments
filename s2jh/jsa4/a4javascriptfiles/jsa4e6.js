const form = document.getElementById('joke-form');
const resultsContainer = document.getElementById('joke-results');

form.addEventListener('submit', async function (event) {
  event.preventDefault();

  const searchTerm = document.getElementById('search').value;

  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(searchTerm)}`);
    if (!response.ok) {
        throw new Error('Failed to fetch jokes.');
    }

    const data = await response.json();

    resultsContainer.innerHTML = '';

    if (data.result.length === 0) {
      resultsContainer.innerHTML = '<p>No jokes found. Try another search term.</p>';
      return;
    }

    data.result.forEach(joke => {
      const article = document.createElement('article');
      const paragraph = document.createElement('p');
      paragraph.textContent = joke.value;
      article.appendChild(paragraph);
      resultsContainer.appendChild(article);
    });
  } catch (error) {
    console.error('Error fetching jokes:', error);
    resultsContainer.innerHTML = `<p>Error: ${error.message}</p>`;
  }
});