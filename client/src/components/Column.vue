<template>
  <div>
    <rename-column />
    <delete-column />
    <add-entry />
    <ul class="column">
      <li class="column-header">
        <div class="edit-click-area" @click="() => showRenameColumnModal(id, title)">
          <div class="column-name">{{ title }}</div>
          <pencil-icon class="icon" />
        </div>
        <div class="delete-click-area" @click="() => showDeleteColumnModal(id, title)">
          <close-icon class="icon" />
        </div>
      </li>
      <li class="column-add-entry" @click="() => showAddEntryModal(id)">Add New Entry</li>
    </ul>
  </div>
  <!--<li v-for="entry in column.entries" v-bind:key="entry.id">
        <entry :name="entry.name" />
  </li>-->
</template>

<style scoped>
.column {
  list-style: none;
  width: 100%;
  padding: 0;
  margin: 0;
}

.column-header {
  padding: 0.75rem 1.25rem;
  border: 0.75px solid rgba(0, 0, 0, 0.125);
  font-weight: 800;
  background: rgba(0, 0, 0, 0.05);
  display: flex;
  width: 100%;
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
</style>

<script>
import { mapActions } from 'vuex';
import draggable from 'vuedraggable';

import PencilIcon from 'vue-material-design-icons/Pencil.vue';
import CloseIcon from 'vue-material-design-icons/Close.vue';

import Entry from './Entry.vue';
import DeleteColumn from './modals/DeleteColumn.vue';
import RenameColumn from './modals/RenameColumn.vue';
import AddEntry from './modals/AddEntry.vue';

export default {
  name: 'Column',
  props: ['title', 'id'],
  components: {
    RenameColumn,
    DeleteColumn,
    AddEntry,
    PencilIcon,
    CloseIcon,
    Entry,
  },
  methods: {
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
