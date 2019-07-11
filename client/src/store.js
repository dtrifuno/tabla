import Vue from 'vue';
import Vuex from 'vuex';

import { getTables, postTable, deleteTable } from './api';
import { fixId } from './util';

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
};

const actions = {
  setToken({ commit }, token) {
    commit('setToken', token);
  },
  async fetchTables({ commit, state }) {
    await getTables(state.token).then((response) => {
      const tables = JSON.parse(response.data);
      const fixedTables = tables.map(fixId);
      commit('setTables', fixedTables);
    });
  },
  async createTable({ commit, state }, title) {
    await postTable(state.token, title).then((response) => {
      const table = JSON.parse(response.data);
      const fixedTable = fixId(table);
      commit('setTables', state.tables.concat(fixedTable));
    });
  },
  async removeTable({ commit, state }, tableId) {
    await deleteTable(state.token, tableId).then((response) => {
      commit('setTables', state.tables.filter(x => x.id !== tableId));
    });
  },
  setCurrentTable({ commit }, table) {
    commit('setCurrentTable', table);
  },
};

const getters = {};

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
});
