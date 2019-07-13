<template>
  <div class="about">
    <add-column />
    <delete-column />
    <rename-table />
    <div class="mx-auto">
      <div @click="showRenameTableModal" class="title-box">
        <h3 class="title">{{this.$store.state.currentTable.name}}</h3>
        <pencil-icon class="title-edit-icon icon-2x" />
      </div>
    </div>
    <ul class="columns">
      <li>
        <ul class="column">
          <li class="column-header">Column 1 Heading</li>
          <entry name="Second Title" />
          <entry
            name="Third title that is much longer than the previous two, and is perhaps a more realistic example of a description?"
          />
          <li class="column-add-entry">ADD NEW ENTRY</li>
        </ul>
      </li>
      <li>
        <ul class="column">
          <li class="column-header">Column 2 Heading</li>
          <li class="column-entry">
            <div class="column-entry-title">First Title</div>
          </li>
          <li class="column-entry">
            <div
              class="column-entry-title"
            >Finish this accursed project that is taking me way too long</div>
          </li>
          <li class="column-entry">Third Title</li>
        </ul>
      </li>
      <li>
        <ul class="column">
          <li class="add-column" @click="showAddColumnModal">Create Column</li>
        </ul>
      </li>
      <ul
        v-for="column in this.$store.state.currentTable.columns"
        v-bind:key="column.id"
        class="column"
      >
        <li class="column-header">
          <div class="edit-click-area">
            <div class="column-name">{{column.name}}</div>
            <pencil-icon class="icon" />
          </div>
          <div class="delete-click-area">
            <close-icon class="icon" />
          </div>
        </li>
        <li>
          <entry name="First Title" />
        </li>
        <li class="column-add-entry">ADD NEW ENTRY</li>
      </ul>
    </ul>
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
}
.columns {
  list-style: none;
  display: flex;
  flex-direction: row;
  padding: 0 0 0 0rem;
}

.column {
  list-style: none;
  display: flex;
  flex-direction: column;
  padding: 0 0 0 2rem;
}

.column-header {
  padding: 0.75rem 1.25rem;
  border: 0.75px solid rgba(0, 0, 0, 0.125);
  font-weight: 800;
  background: rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: row;
  align-items: center;
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

.edit-click-area:hover .icon {
  color: green;
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
}

.column-entry-title {
  font-weight: 600;
  text-align: center;
}

.title-box:hover {
  cursor: pointer;
}

.title-box:hover .title-edit-icon {
  color: green;
}
</style>


<script>
import { mapActions } from 'vuex';
import PencilIcon from 'vue-material-design-icons/Pencil.vue';
import CloseIcon from 'vue-material-design-icons/Close.vue';

import AddColumn from '../components/AddColumn.vue';
import RenameTable from '../components/RenameTable.vue';
import Entry from '../components/Entry.vue';

export default {
  name: 'Table',
  components: {
    AddColumn,
    RenameTable,
    Entry,
    PencilIcon,
    CloseIcon,
  },
  methods: {
    showAddColumnModal() {
      this.$modal.show('add-column', {
        height: 'auto',
      });
    },
    showRenameTableModal() {
      this.$modal.show('rename-table', {
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
  },
};
</script>
