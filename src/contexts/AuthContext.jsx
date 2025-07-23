import React, { createContext, useState, useEffect, useContext } from 'react';
import { useDispatch } from 'react-redux';
import { setUser, clearUser } from '../redux/slices/authSlice';
import api from '../services/api';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const dispatch = useDispatch();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('authToken');
    if (token) {
      api.get('/auth/verify/', {
        headers: { Authorization: `Bearer ${token}` }
      })
        .then(res => dispatch(setUser({ token, ...res.data.user })))
        .catch(() => dispatch(clearUser()))
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, [dispatch]);

  const login = async (credentials) => {
    const response = await api.post('/auth/login/', credentials);
    localStorage.setItem('authToken', response.data.token);
    dispatch(setUser({ token: response.data.token, ...response.data.user }));
  };

  const logout = () => {
    localStorage.removeItem('authToken');
    dispatch(clearUser());
  };

  return (
    <AuthContext.Provider value={{ login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
