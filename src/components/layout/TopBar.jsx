import React from 'react';
import OfflineIndicator from './common/OfflineIndicator';
import UserMenu from './UserMenu';

function TopBar() {
  return (
    <header className="top-bar">
      <div className="logo">Mutare RDC GIS</div>
      <div className="top-bar-actions">
        <OfflineIndicator />
        <UserMenu />
      </div>
    </header>
  );
}

export default TopBar;