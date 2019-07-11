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

// /table
function postTable(token, tableName) {
  return axios.post(
    'http://localhost:5000/table',
    {
      tableName,
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
function postColumn(token, tableId, columnName) {
  return (
    axios.post('http://localhost:5000/column'),
    {
      tableId,
      columnName,
    },
    {
      headers: { Authorization: `Bearer ${token}` },
    }
  );
}

export {
 login, registerUser, postTable, deleteTable, getTables, getTable, postColumn 
};
