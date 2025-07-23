import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  viewport: {
    center: [-18.9724, 32.6706],
    zoom: 12
  },
  infrastructureData: null,
  selectedFeature: null,
  wardBoundaries: null
};

export const mapSlice = createSlice({
  name: 'map',
  initialState,
  reducers: {
    setViewport: (state, action) => {
      state.viewport = action.payload;
    },
    setInfrastructureData: (state, action) => {
      state.infrastructureData = action.payload;
    },
    setSelectedFeature: (state, action) => {
      state.selectedFeature = action.payload;
    },
    setWardBoundaries: (state, action) => {
      state.wardBoundaries = action.payload;
    }
  }
});

export const { setViewport, setInfrastructureData, setSelectedFeature, setWardBoundaries } = mapSlice.actions;
export default mapSlice.reducer;
