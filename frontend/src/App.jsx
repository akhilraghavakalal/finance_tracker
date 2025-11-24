import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('Loading...')
  const [health, setHealth] = useState(null)

  useEffect(() => {
    // Fetch from root endpoint
    fetch('http://localhost:8000/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => setMessage('Error: ' + err.message))

    // Fetch from health endpoint
    fetch('http://localhost:8000/api/v1/health')
      .then(res => res.json())
      .then(data => setHealth(data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div className="App">
      <h1>Finance Tracker</h1>
      <div className="card">
        <h2>Backend Connection Test</h2>
        <p><strong>Root Endpoint:</strong> {message}</p>
        {health && (
          <p><strong>Health Check:</strong> {health.status} - {health.message}</p>
        )}
      </div>
    </div>
  )
}

export default App