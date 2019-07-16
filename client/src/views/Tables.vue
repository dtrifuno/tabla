<template>
  <div>
    <add-table />
    <delete-table />
    <div class="list-group col-10 col-lg-3 mx-auto">
      <div @click="addTableModal" class="new-table-item">Create New Table</div>
      <br />
      <draggable v-model="tables" class="table-list">
        <table-entry
          v-for="item in tables"
          :name="item.name"
          :id="item.id"
          :onClickTitle="() => titleClick(item.id, item.name)"
          :onClickDelete="() => deleteClick(item.id, item.name)"
          class="table-item"
          v-bind:key="item.id"
        />
      </draggable>
    </div>
  </div>
</template>

<style scoped>
.table-list {
  list-style: none;
  margin: 0 0 0 0;
  padding: 0 0 0 0;
}

.list-group {
  padding: 0;
}

.new-table-item {
  padding: 0.65rem 1.25rem;
  font-weight: 600;
  border: 1px solid rgba(0, 0, 0, 0.125);
  cursor: pointer;
  user-select: none;
}

.table-list .table-item {
  padding: 0 0.25rem 0 0.75rem;
  border: 0.75px solid rgba(0, 0, 0, 0.125);
  background-color: transparent;
  cursor: pointer;
  text-align: left;
}

.table-item:hover,
.new-table-item:hover {
  background: rgba(40, 167, 69, 0.2);
}

.table-item:active,
.new-table-item:active {
  background: rgba(40, 167, 69, 0.4);
}
</style>


<script>
import { mapActions } from 'vuex';
import draggable from 'vuedraggable';

import { getTable } from '../api';

import AddTable from '../components/AddTable';
import DeleteTable from '../components/DeleteTable';
import TableEntry from '../components/TableEntry';

export default {
  name: 'Tables',
  components: {
    AddTable,
    DeleteTable,
    TableEntry,
    draggable,
  },
  computed: {
    tables: {
      get() {
        return this.$store.state.tables;
      },
      set(value) {
        this.reorderTables(value);
      },
    },
  },
  methods: {
    ...mapActions(['setTables', 'setCurrentTable', 'reorderTables']),
    addTableModal() {
      this.$modal.show('add-table', {
        height: 'auto',
      });
    },
    async titleClick(id) {
      await this.setCurrentTable(id).then(() => this.$router.push({ path: '/table' }),);
    },
    deleteClick(id, name) {
      this.$modal.show('delete-table', {
        tableName: name,
        tableId: id,
      });
    },
  },
};
</script>
