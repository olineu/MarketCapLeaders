import React from 'react';

const CompanyList = () => {
  // Placeholder data (you'll replace this with real data from your backend)
  const companies = [
    { id: 1, name: 'Company A', rank: 1, marketCap: 1000000 },
    { id: 2, name: 'Company B', rank: 2, marketCap: 900000 },
    { id: 3, name: 'Company C', rank: 3, marketCap: 800000 },
    // Add more companies here
  ];

  return (
    <div className="company-list">
      <h2>Top Companies by Market Cap</h2>
      <ul>
        {companies.map((company) => (
          <li key={company.id}>
            <strong>{company.name}</strong> (Rank: {company.rank}) - Market Cap: ${company.marketCap}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CompanyList;
