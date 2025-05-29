import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [watchlist, setWatchlist] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/watchlist/')
      .then(response => setWatchlist(response.data))
      .catch(error => console.error('Error fetching watchlist:', error));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Watchlist</h1>
      <ul>
        {watchlist.map(item => (
          <li key={item.id}>{item.symbol}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
