import PouchDB from 'pouchdb-browser';

export const offlineDB = new PouchDB('offline_edits');

export const queueOfflineEdit = (editData) => {
  return offlineDB.put({
    _id: `edit_${Date.now()}`,
    type: 'feature_edit',
    payload: editData,
    status: 'pending',
    timestamp: new Date().toISOString()
  });
};
