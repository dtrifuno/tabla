<template>
  <div class="about">
    <rename-table />
    <add-column />
    <delete-column />
    <rename-column />
    <add-entry />
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
      <ul
        v-for="column in this.$store.state.currentTable.columns"
        v-bind:key="column.id"
        class="column col-10 col-xl-3"
      >
        <li class="column-header">
          <div class="edit-click-area" @click="() => showRenameColumnModal(column.id, column.name)">
            <div class="column-name">{{column.name}}</div>
            <pencil-icon class="icon" />
          </div>
          <div
            class="delete-click-area"
            @click="() => showDeleteColumnModal(column.id, column.name)"
          >
            <close-icon class="icon" />
          </div>
        </li>
        <li v-for="entry in column.entries" v-bind:key="entry.id">
          <entry :name="entry.name" />
        </li>
        <li class="column-add-entry" @click="() => showAddEntryModal(column.id)">Add New Entry</li>
      </ul>
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

.column-header {
  padding: 0.75rem 1.25rem;
  border: 0.75px solid rgba(0, 0, 0, 0.125);
  font-weight: 800;
  background: rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  user-select: none;
}

.column-name {
  flex: 1 0 auto;
}

.edit-click-area {
  display: flex;
  flex-direction: row;
  align-items: center;
  flex: 1 0 auto;
  cursor: pointer;
}

.icon {
  flex: 0 1 auto;
}

.edit-click-area:hover {
  color: #28a745;
}
.edit-click-area:hover .icon {
  color: #28a745;
}

.delete-click-area {
  display: flex;
  align-content: center;
  cursor: pointer;
}

.delete-click-area:hover .icon {
  color: brown;
}

.column-entry {
  padding: 0.75rem 1.25rem;
  border: 1px solid rgba(0, 0, 0, 0.125);
  width: 20vw;
}

.column-add-entry {
  padding: 0.75rem 1.25rem;
  border: 1px solid rgba(0, 0, 0, 0.125);
  cursor: pointer;
  font-weight: 600;
  user-select: none;
}

.column-add-entry:hover {
  background: rgba(40, 167, 69, 0.2);
}
.column-add-entry:active {
  background: rgba(40, 167, 69, 0.4);
}

.column-entry-title {
  font-weight: 600;
  text-align: center;
}

.title-box:hover {
  cursor: pointer;
  color: #28a745;
}

.title-box:hover .title-edit-icon {
  color: #28a745;
}
</style>


<script>
import { mapActions } from 'vuex';
import draggable from 'vuedraggable';

import PencilIcon from 'vue-material-design-icons/Pencil.vue';
import CloseIcon from 'vue-material-design-icons/Close.vue';

import RenameTable from '../components/modals/RenameTable.vue';
import AddColumn from '../components/modals/AddColumn.vue';
import DeleteColumn from '../components/modals/DeleteColumn.vue';
import RenameColumn from '../components/modals/RenameColumn.vue';
import AddEntry from '../components/modals/AddEntry.vue';
import Entry from '../components/Entry.vue';

export default {
  name: 'Table',
  components: {
    RenameTable,
    AddColumn,
    DeleteColumn,
    RenameColumn,
    AddEntry,
    Entry,
    draggable,
    PencilIcon,
    CloseIcon,
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
    showDeleteColumnModal(columnId, columnName) {
      this.$modal.show('delete-column', {
        height: 'auto',
        columnId,
        columnName,
      });
    },
    showRenameColumnModal(columnId, columnName) {
      this.$modal.show('rename-column', {
        height: 'auto',
        columnId,
        columnName,
      });
    },
    showAddEntryModal(columnId) {
      this.$modal.show('add-entry', {
        height: 'auto',
        columnId,
      });
    },
  },
};
</script>
