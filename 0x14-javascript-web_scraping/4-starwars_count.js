#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else {
    const filmsData = JSON.parse(body);

    const moviesWithWedgeAntilles = filmsData.results.filter((movie) => {
      return movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });

    console.log(`Number of movies with Wedge Antilles: ${moviesWithWedgeAntilles.length}`);
  }
});

