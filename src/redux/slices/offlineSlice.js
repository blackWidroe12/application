import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  status: 'online'
};

export const offlineSlice = createSlice({
  name: 'offline',
  initialState,
  reducers: {
    setOfflineStatus: (state, action) => {
      state.status = action.payload;
    }
  }
});

export const { setOfflineStatus } = offlineSlice.actions;
export default offlineSlice.reducer;
