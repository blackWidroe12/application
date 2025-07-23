import React from 'react';
import { MapContainer as LeafletMap, TileLayer } from 'react-leaflet';
import { useSelector } from 'react-redux';
import InfrastructureLayer from '../map/InfrastructureLayer';
import WardBoundaries from '../map/WardBoundaries';
import 'leaflet/dist/leaflet.css';

const MapContainer = () => {
  const viewport = useSelector(state => state.map.viewport);

  return (
    <div className="map-container">
      <LeafletMap
        center={viewport.center}
        zoom={viewport.zoom}
        style={{ height: '100%', width: '100%' }}
        zoomControl={true}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; OpenStreetMap contributors'
        />
        <WardBoundaries />
        <InfrastructureLayer />
      </LeafletMap>
    </div>
  );
};

export default MapContainer;
