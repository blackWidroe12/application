import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000',
  timeout: 30000
});

api.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export const fetchInfrastructure = async (params = {}) => {
  const response = await api.get('/api/infrastructure/', { params });
  return response.data;
};

export const fetchWardBoundaries = async () => {
  const response = await api.get('/api/wards/geojson/');
  return response.data;
};

export default api;
