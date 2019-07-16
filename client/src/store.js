import Vue from 'vue';
import Vuex from 'vuex';

import {
  getTables,
  putTables,
  getTable,
  postTable,
  putTable,
  deleteTable,
  postColumn,
  putColumn,
  deleteColumn,
  postEntry,
} from './api';
import { sortByPrev, prevFromOrder, promiseForEach } from './util';

Vue.use(Vuex);

const state = {
  token: '',
  tables: [],
  currentTable: {},
};

const mutations = {
  setToken(state, token) {
    state.token = token;
  },
  setTables(state, tables) {
    state.tables = tables;
  },
  removeTable(state, tableId) {
    state.tables = state.tables.filter(x => x.id !== tableId);
  },
  setCurrentTable(state, table) {
    state.currentTable = table;
  },
  addColumn(state, column) {
    state.currentTable.columns.push(column);
  },
  setColumns(state, columns) {
    state.currentTable.columns = columns;
  },
  removeColumn(state, columnId) {
    const { currentTable } = state;
    currentTable.columns = currentTable.columns.filter(x => x.id !== columnId);
  },
  editColumn(state, newColumn) {
    const { id } = newColumn;
    const { columns } = state.currentTable;
    const column = columns.filter(x => x.id === id)[0];
    Object.assign(column, newColumn);
  },
  addEntry(state, { entry, columnId }) {
    const { columns } = state.currentTable;
    const column = columns.filter(x => x.id === columnId)[0];
    column.entries.push(entry);
  },
};

const actions = {
  setToken({ commit }, token) {
    commit('setToken', token);
  },
  async fetchTables({ commit, state }) {
    await getTables(state.token).then((response) => {
      const tables = JSON.parse(response.data);
      const sortedTables = sortByPrev(tables);
      commit('setTables', sortedTables);
    });
  },
  async reorderTables({ state, commit }, tables) {
    const newTables = prevFromOrder(tables);
    const tablesToPut = [];
    for (let i = 0; i < tables.length; i += 1) {
      if (tables[i].prev !== newTables[i].prev) {
        tablesToPut.push(newTables[i]);
      }
    }
    promiseForEach(tablesToPut, table => putTable(state.token, table)).then(
      commit('setTables', newTables),
    );
  },
  async createTable({ commit, state }, title) {
    const prev = state.tables.length ? state.tables.slice(-1)[0].id : null;
    await postTable(state.token, title, prev).then((response) => {
      const table = JSON.parse(response.data);
      commit('setTables', state.tables.concat(table));
    });
  },
  async removeTable({ commit, state, dispatch }, tableId) {
    await deleteTable(state.token, tableId)
      .then(commit('removeTable', tableId))
      .then(dispatch('reorderTables', state.tables));
  },
  async renameCurrentTable({ commit, state }, name) {
    const table = { ...state.currentTable };
    table.name = name;
    await putTable(state.token, table).then((response) => {
      const newTable = JSON.parse(response.data);
      commit('setCurrentTable', { ...state.currentTable, name: newTable.name });
    });
  },
  async createColumn({ commit, state }, name) {
    const tableId = state.currentTable.id;
    const { columns } = state.currentTable;
    console.log(columns);
    const prev = columns.length ? columns.slice(-1)[0].id : null;
    await postColumn(state.token, tableId, name, prev).then((response) => {
      const column = JSON.parse(response.data);
      commit('addColumn', { ...column, entries: [] });
    });
  },
  async reorderColumns({ state, commit }, columns) {
    const newColumns = prevFromOrder(columns);
    const columnsToPut = [];
    for (let i = 0; i < columns.length; i += 1) {
      if (columns[i].prev !== newColumns[i].prev) {
        columnsToPut.push(newColumns[i]);
      }
    }
    promiseForEach(columnsToPut, column => putColumn(state.token, column)).then(
      commit('setColumns', newColumns),
    );
  },
  async removeColumn({ commit, dispatch, state }, columnId) {
    await deleteColumn(state.token, columnId)
      .then(commit('removeColumn', columnId))
      .then(dispatch('reorderColumns', state.currentTable.columns));
  },
  // HERE
  async renameColumn({ commit, state }, { columnId, name }) {
    await putColumn(state.token, columnId, name).then((response) => {
      const newColumn = JSON.parse(response.data);
      commit('editColumn', newColumn);
    });
  },
  async createEntry({ commit, state }, { columnId, name }) {
    const column = state.currentTable.columns.filter(x => x.id === columnId)[0];
    const order = column.length;
    await postEntry(state.token, columnId, name, order).then((response) => {
      console.log(response.data);
      const entry = JSON.parse(response.data);
      commit('addEntry', { columnId, entry });
    });
  },
  async setCurrentTable({ commit, state }, tableId) {
    await getTable(state.token, tableId).then((response) => {
      const table = JSON.parse(response.data);
      table.columns = sortByPrev(table.columns);
      commit('setCurrentTable', table);
    });
  },
};

const getters = {};

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
});
