import React from 'react';
import { Provider } from 'react-redux';
import { AuthProvider } from '../../contexts/AuthContext';
import TopBar from './TopBar';
import ControlPanel from './ControlPanel';
import MapContainer from './MapContainer';
import store from '../../redux/store';

function App() {
  return (
    <Provider store={store}>
      <AuthProvider>
        <div className="app-container">
          <TopBar />
          <div className="main-content">
            <ControlPanel />
            <div className="map-panel">
              <MapContainer />
            </div>
          </div>
          
          {/* Real-time notifications, sync status, alerts would go here */}
        </div>
      </AuthProvider>
    </Provider>
  );
}

export default App;
