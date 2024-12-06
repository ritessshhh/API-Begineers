const BASE_URL = "http://127.0.0.1:5000";

// Home Route
fetch(`${BASE_URL}/`)
  .then(response => response.text())
  .then(data => console.log("Home Route Response:", data))
  .catch(error => console.error("Error:", error));

// Current Time
fetch(`${BASE_URL}/time`)
  .then(response => response.json())
  .then(data => console.log("Current Time Response:", data))
  .catch(error => console.error("Error:", error));

// Current Date
fetch(`${BASE_URL}/date`)
  .then(response => response.json())
  .then(data => console.log("Current Date Response:", data))
  .catch(error => console.error("Error:", error));

// Greeting
fetch(`${BASE_URL}/greet/Ritesh`)
  .then(response => response.json())
  .then(data => console.log("Greeting Response:", data))
  .catch(error => console.error("Error:", error));

// API Status
fetch(`${BASE_URL}/status`)
  .then(response => response.json())
  .then(data => console.log("Status Response:", data))
  .catch(error => console.error("Error:", error));