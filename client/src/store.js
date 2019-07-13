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
} from './api';
import { sortByOrder, orderFromPosition } from './util';

Vue.use(Vuex);

const state = {
  token: '',
  tables: [],
  currentTable: {},
};

const mutations = {
  setToken(state, token) {
    state.token = token;
    console.log(token);
  },
  setTables(state, tables) {
    state.tables = tables;
    console.log(tables);
  },
  setCurrentTable(state, table) {
    state.currentTable = table;
    console.log(table);
  },
  addColumn(state, column) {
    state.currentTable.columns.push(column);
    console.log(column);
  },
};

const actions = {
  setToken({ commit }, token) {
    commit('setToken', token);
  },
  async fetchTables({ commit, state }) {
    await getTables(state.token).then((response) => {
      const tables = JSON.parse(response.data);
      const sortedTables = sortByOrder(tables);
      commit('setTables', sortedTables);
    });
  },
  async reorderTables({ commit, state }, tables) {
    const newTables = orderFromPosition(tables);
    const tablesToPut = [];
    for (let i = 0; i < newTables.length; i += 1) {
      if (tables[i].order !== newTables[i].order) {
        tablesToPut.push({ ...newTables[i] });
      }
    }
    commit('setTables', newTables);
    putTables(state.token, tablesToPut);
  },
  async createTable({ commit, state }, title) {
    const order = state.tables.length;
    await postTable(state.token, title, order).then((response) => {
      const table = JSON.parse(response.data);
      commit('setTables', state.tables.concat(table));
    });
  },
  async removeTable({ commit, state }, tableId) {
    await deleteTable(state.token, tableId).then((response) => {
      commit('setTables', state.tables.filter(x => x.id !== tableId));
    });
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
    const order = state.currentTable.columns.length;
    await postColumn(state.token, tableId, name, order).then((response) => {
      const column = JSON.parse(response.data);
      commit('addColumn', { ...column, entries: [] });
    });
  },
  async setCurrentTable({ commit, state }, tableId) {
    await getTable(state.token, tableId).then((response) => {
      const table = JSON.parse(response.data);
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
