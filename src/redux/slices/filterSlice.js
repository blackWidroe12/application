import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  infrastructureTypes: {
    road: true,
    clinic: true,
    school: true
  },
  ward: null,
  quickFilter: null,
  searchQuery: ''
};

export const filterSlice = createSlice({
  name: 'filters',
  initialState,
  reducers: {
    toggleInfrastructureType: (state, action) => {
      const type = action.payload;
      state.infrastructureTypes[type] = !state.infrastructureTypes[type];
    },
    setWardFilter: (state, action) => {
      state.ward = action.payload;
    },
    setQuickFilter: (state, action) => {
      state.quickFilter = action.payload;
    },
    setSearchQuery: (state, action) => {
      state.searchQuery = action.payload;
    },
    resetFilters: () => initialState
  }
});

export const {
  toggleInfrastructureType,
  setWardFilter,
  setQuickFilter,
  setSearchQuery,
  resetFilters
} = filterSlice.actions;

export default filterSlice.reducer;
