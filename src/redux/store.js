import { configureStore } from '@reduxjs/toolkit';
import mapReducer from './slices/mapSlice';
import filterReducer from './slices/filterSlice';
import authReducer from './slices/authSlice';

export const store = configureStore({
  reducer: {
    map: mapReducer,
    filters: filterReducer,
    auth: authReducer
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false
    })
});

export default store;
