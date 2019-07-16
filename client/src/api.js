import axios from 'axios';

const url = '/api';

// /login
function login(email, password) {
  return axios.post(`${url}/login`, {
    email,
    password,
  });
}

// /registration
function registerUser(email, password) {
  return axios.post(`${url}/register`, {
    email,
    password,
  });
}

// /tables
function getTables(token) {
  return axios.get(`${url}/tables`, {
    headers: { Authorization: `Bearer ${token}` },
  });
}

// /table
function postTable(token, name, prev) {
  return axios.post(
    `${url}/table`,
    {
      name,
      prev,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

function putTable(token, table) {
  return axios.put(
    `${url}/table/${table.id}`,
    {
      ...table,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

function deleteTable(token, tableId) {
  return axios.delete(`${url}/table/${tableId}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
}

function getTable(token, tableId) {
  return axios.get(`${url}/table/${tableId}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
}

// /column
function postColumn(token, tableId, name, prev) {
  return axios.post(
    `${url}/column`,
    {
      tableId,
      name,
      prev,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

function putColumn(token, column) {
  return axios.put(
    `${url}/column/${column.id}`,
    {
      ...column,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

function deleteColumn(token, columnId) {
  return axios.delete(`${url}/column/${columnId}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
}

// TODO

function postEntry(token, columnId, name, order) {
  return axios.post(
    `${url}/entry`,
    { columnId, name, order },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

export {
  login,
  registerUser,
  postTable,
  deleteTable,
  getTables,
  getTable,
  putTable,
  postColumn,
  putColumn,
  deleteColumn,
  postEntry,
};
