import React from 'react';

const INFRA_TYPES = [
  { id: 'road', label: 'Roads', icon: '🛣️' },
  { id: 'clinic', label: 'Clinics', icon: '🏥' },
  { id: 'school', label: 'Schools', icon: '🏫' }
];

export default function InfrastructureFilter() {
  return (
    <div className="filter-section">
      <h3>Infrastructure Types</h3>
      <div className="type-grid">
        {INFRA_TYPES.map(type => (
          <div key={type.id} className="type-card">
            <span className="type-icon">{type.icon}</span>
            {type.label}
          </div>
        ))}
      </div>
    </div>
  );
}
