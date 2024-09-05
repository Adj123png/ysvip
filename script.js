async function scrapeMovie() {
    const url = document.getElementById('movie-url').value;
    const response = await fetch(`https://your-api-endpoint.com/scrape?url=${encodeURIComponent(url)}`);
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data, null, 2);
}
