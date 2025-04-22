

const http = require('http');

http.get('http://localhost:3000', (res) => {
  let data = '';

  // Collect response chunks
  res.on('data', (chunk) => {
    data += chunk;
  });

  // On response end
  res.on('end', () => {
    console.log('Response from server:', data);
  });
}).on('error', (err) => {
  console.error('Error:', err.message);
});
