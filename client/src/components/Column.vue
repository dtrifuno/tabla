<template>
  <div>
    <ul class="column">
      <li class="column-header">
        <div class="edit-click-area" @click="() => showRenameColumnModal(column)">
          <div class="column-name">{{ shortTitle }}</div>
          <pencil-icon class="icon" />
        </div>
        <div class="delete-click-area" @click="() => showDeleteColumnModal(column)">
          <close-icon class="icon" />
        </div>
      </li>
      <li>
        <draggable v-model="entries" group="entries">
          <transition-group type="transition" name="flip-list" class="draggable-area">
            <entry
              v-for="entry in entries"
              :name="entry.name"
              v-bind:key="entry.id"
              :onClickDelete="() => showDeleteEntryModal(column.id, entry)"
            />
          </transition-group>
        </draggable>
      </li>
      <li class="column-add-entry" @click="() => showAddEntryModal(column.id)">Add New Entry</li>
    </ul>
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

.icon {
  flex: 0 1 auto;
}

.edit-click-area {
  display: flex;
  flex-direction: row;
  align-items: center;
  flex: 1 0 auto;
  cursor: pointer;

  &:hover {
    color: #28a745;
  }

  &:hover .icon {
    color: #28a745;
  }
}

.delete-click-area {
  display: flex;
  align-content: center;
  cursor: pointer;

  &:hover .icon {
    color: brown;
  }
}

.column-add-entry {
  padding: 0.75rem 1.25rem;
  border: 1px solid rgba(0, 0, 0, 0.125);
  cursor: pointer;
  font-weight: 600;
  user-select: none;

  &:hover {
    background: rgba(40, 167, 69, 0.2);
  }

  &:active {
    background: rgba(40, 167, 69, 0.4);
  }
}

.draggable-area {
  display: block;
  min-height: 0.01px;
  width: 100%;
}
</style>

<script>
import { mapActions } from 'vuex';
import draggable from 'vuedraggable';

import PencilIcon from 'vue-material-design-icons/Pencil.vue';
import CloseIcon from 'vue-material-design-icons/Close.vue';
import { shorten } from '../util';

import Entry from './Entry.vue';

export default {
  name: 'Column',
  props: ['column'],
  components: {
    PencilIcon,
    CloseIcon,
    Entry,
    draggable,
  },
  computed: {
    shortTitle() {
      return shorten(this.column.name, 21);
    },
    entries: {
      get() {
        return this.$store.state.currentTable.columns.filter((x) => x.id === this.column.id)[0]
          .entries;
      },
      set(value) {
        this.reorderEntries({ columnId: this.column.id, entries: value });
      },
    },
  },
  methods: {
    ...mapActions(['reorderEntries']),
    showDeleteColumnModal(column) {
      this.$modal.show('delete-column', {
        height: 'auto',
        clickToClose: false,
        column,
      });
    },
    showRenameColumnModal(column) {
      this.$modal.show('rename-column', {
        height: 'auto',
        clickToClose: false,
        column,
      });
    },
    showAddEntryModal(columnId) {
      this.$modal.show('add-entry', {
        height: 'auto',
        clickToClose: false,
        columnId,
      });
    },
    showDeleteEntryModal(columnId, entry) {
      this.$modal.show('delete-entry', {
        height: 'auto',
        clickToClose: false,
        entry,
        columnId,
      });
    },
  },
};
</script>
