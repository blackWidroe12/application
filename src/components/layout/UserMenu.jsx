// src/components/layout/UserMenu.jsx
import React, { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { IconButton, Menu, MenuItem } from '@mui/material';
import { AccountCircle } from '@mui/icons-material';

export default function UserMenu() {
  const [anchorEl, setAnchorEl] = useState(null);
  const { user, logout } = useAuth();

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div className="user-menu">
      <IconButton onClick={handleMenuOpen} color="inherit">
        <AccountCircle fontSize="large" />
      </IconButton>
      
      <Menu
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <MenuItem disabled>{user?.username || 'Guest'}</MenuItem>
        <MenuItem disabled>Role: {user?.role || 'public'}</MenuItem>
        <MenuItem onClick={logout}>Logout</MenuItem>
      </Menu>
    </div>
  );
}