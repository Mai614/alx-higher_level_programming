#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else {
    const movieData = JSON.parse(body);

    if (movieData.detail === 'Not found') {
      console.error(`Movie with ID ${movieId} not found.`);
    } else {
      console.log(`Title: ${movieData.title}`);
    }
  }
});

