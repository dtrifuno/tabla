<template>
  <div class="about">
    <rename-table />
    <add-column />
    <div class="mx-auto">
      <div
        @click="() => showRenameTableModal(this.$store.state.currentTable.id, this.$store.state.currentTable.name)"
        class="title-box"
      >
        <h3 class="title">{{this.$store.state.currentTable.name}}</h3>
        <pencil-icon class="title-edit-icon icon-2x" />
      </div>
    </div>
    <div class="add-column-btn col-10 col-xl-3 mx-auto" @click="showAddColumnModal">Create Column</div>
    <draggable v-model="columns" class="columns">
      <column
        v-for="column in columns"
        v-bind:key="column.id"
        :title="column.name"
        :id="column.id"
        class="column col-10 col-xl-2"
      />
    </draggable>
  </div>
</template>

<style scoped>
.title-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: 0 0 1.5rem 0;
}

.title-box:hover {
  cursor: pointer;
  color: #28a745;
}

.title-box:hover .title-edit-icon {
  color: #28a745;
}

.title {
  padding: 0;
  margin: 0.5rem 0.3rem 0 0;
  user-select: none;
}

.add-column-btn {
  padding: 0.65rem 1.25rem;
  font-weight: 600;
  border: 1px solid rgba(0, 0, 0, 0.125);
  cursor: pointer;
  margin: 1rem;
  user-select: none;
}

.add-column-btn:hover {
  background: rgba(40, 167, 69, 0.2);
}

.add-column-btn:active {
  background: rgba(40, 167, 69, 0.4);
}

.columns {
  list-style: none;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding: 0 0 0 0rem;
}

.column {
  display: flex;
  flex-direction: column;
  padding: 1rem 1rem 0 1rem;
  list-style: none;
}

@media (max-width: 1199px) {
  .columns {
    flex-direction: column;
  }

  .column {
    padding: 0 0 1.5rem 0;
    margin-left: auto !important;
    margin-right: auto !important;
  }
}
</style>

<script>
import { mapActions } from 'vuex';
import draggable from 'vuedraggable';

import PencilIcon from 'vue-material-design-icons/Pencil.vue';

import Column from '../components/Column.vue';
import RenameTable from '../components/modals/RenameTable.vue';
import AddColumn from '../components/modals/AddColumn.vue';

export default {
  name: 'Table',
  components: {
    Column,
    RenameTable,
    AddColumn,
    draggable,
    PencilIcon,
  },
  computed: {
    columns: {
      get() {
        return this.$store.state.currentTable.columns;
      },
      set(value) {
        this.reorderColumns(value);
      },
    },
  },
  methods: {
    ...mapActions(['reorderColumns']),
    showRenameTableModal(tableId, tableName) {
      this.$modal.show('rename-table', {
        height: 'auto',
        tableId,
        tableName,
      });
    },
    showAddColumnModal() {
      this.$modal.show('add-column', {
        height: 'auto',
      });
    },
  },
};
</script>
