import React from 'react';
import './App.css'; // You can create an App.css file for styling

// Import the CompanyList component
import CompanyList from './CompanyList'; // Make sure the path is correct

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Market Cap Leaders</h1>
      </header>
      <main>
        {/* Company List Component */}
        <CompanyList />
      </main>
    </div>
  );
}

export default App;
