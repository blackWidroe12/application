// src/components/common/OfflineIndicator.jsx
import React from 'react';
import { useOffline } from '../../hooks/useOffline';

export default function OfflineIndicator() {
  const { status } = useOffline();
  
  return (
    <div className={`offline-indicator ${status}`}>
      {status === 'online' ? '🟢 Online' : 
       status === 'offline' ? '🔴 Offline' : '🔄 Syncing...'}
    </div>
  );
}
