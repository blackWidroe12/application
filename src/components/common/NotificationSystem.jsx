import React from 'react';
import { useSelector } from 'react-redux';
import { Snackbar, Alert } from '@mui/material';

export default function NotificationSystem() {
  const notifications = useSelector(state => state.notifications);
  
  return (
    <>
      {notifications.map((notification) => (
        <Snackbar
          key={notification.id}
          open={true}
          autoHideDuration={6000}
          anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
        >
          <Alert severity={notification.type} variant="filled">
            {notification.message}
          </Alert>
        </Snackbar>
      ))}
    </>
  );
}