import api from './api';

export const login = async (credentials) => {
  const response = await api.post('/auth/login/', credentials);
  return response.data;
};

export const verifyToken = async (token) => {
  const response = await api.get('/auth/verify/', {
    headers: { Authorization: `Bearer ${token}` }
  });
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('authToken');
};
