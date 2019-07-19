<template>
  <div>
    <h4>Tables</h4>
    <br />
    <add-table />
    <delete-table />
    <div class="list-group mx-auto">
      <div @click="addTableModal" class="new-table-item">Create New Table</div>
      <br />
      <draggable v-model="tables" class="table-list">
        <transition-group type="transition" name="flip-list">
          <table-entry
            v-for="item in tables"
            :name="item.name"
            :id="item.id"
            :onClickTitle="() => titleClick(item.id, item.name)"
            :onClickDelete="() => deleteClick(item.id, item.name)"
            class="table-item"
            v-bind:key="item.id"
          />
        </transition-group>
      </draggable>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.flip-list-move {
  transition: transform 0.5s;
}

.flip-list-enter-active,
.flip-list-leave-active {
  transition: opacity 0.5s;
}
.flip-list-enter,
.flip-list-leave-to {
  opacity: 0;
}

.list-group {
  padding: 0;
  width: 50rem;
}

@media only screen and (max-width: 1000px) {
  .list-group {
    width: 80%;
  }
}

.new-table-item {
  padding: 0.65rem 1.25rem;
  font-weight: 600;
  border: 1px solid rgba(0, 0, 0, 0.125);
  cursor: pointer;
  user-select: none;
}

.table-list {
  list-style: none;
  margin: 0 0 0 0;
  padding: 0 0 0 0;

  .table-item {
    padding: 0 0.25rem 0 0.75rem;
    border: 0.75px solid rgba(0, 0, 0, 0.125);
    background-color: transparent;
    cursor: pointer;
    text-align: left;
    background-color: white;
  }
}

.table-item:hover,
.new-table-item:hover {
  background: rgb(212, 237, 218);
}

.table-item:active,
.new-table-item:active {
  background: rgb(169, 220, 181);
}
</style>

<script>
import { mapActions } from 'vuex';
import draggable from 'vuedraggable';

import AddTable from '../components/modals/AddTable.vue';
import DeleteTable from '../components/modals/DeleteTable.vue';

import TableEntry from '../components/TableEntry.vue';

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
      this.$modal.show('add-table');
    },
    async titleClick(id) {
      await this.setCurrentTable(id).then(() => this.$router.push({ path: '/table' }));
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
