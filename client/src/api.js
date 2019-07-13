import axios from 'axios';

// /login
function login(email, password) {
  return axios.post('http://localhost:5000/login', {
    email,
    password,
  });
}

// /registration
function registerUser(email, password) {
  return axios.post('http://localhost:5000/registration', {
    email,
    password,
  });
}

// /tables
function getTables(token) {
  return axios.get('http://localhost:5000/tables', {
    headers: { Authorization: `Bearer ${token}` },
  });
}

function putTables(token, tables) {
  return axios.put(
    'http://localhost:5000/tables',
    {
      tables,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

// /table
function postTable(token, name, order) {
  return axios.post(
    'http://localhost:5000/table',
    {
      name,
      order,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

function putTable(token, table) {
  return axios.put(
    `http://localhost:5000/table/${table.id}`,
    {
      ...table,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    },
  );
}

function deleteTable(token, tableId) {
  return axios.delete(
    `http://localhost:5000/table/${tableId}`,
    {
      headers: { Authorization: `Bearer ${token}` },
    },
    { tableId },
  );
}

function getTable(token, tableId) {
  return axios.get(`http://localhost:5000/table/${tableId}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
}

// /column
function postColumn(token, tableId, name, order) {
  return axios.post(
    'http://localhost:5000/column',
    {
      tableId,
      name,
      order,
    },
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
  putTables,
  getTable,
  putTable,
  postColumn,
};
