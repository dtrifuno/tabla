<template>
  <div class="about">
    <rename-table />
    <add-column />
    <rename-column />
    <delete-column />
    <add-entry />
    <delete-entry />
    <div class="mx-auto">
      <div
        @click="
          () =>
            showRenameTableModal(
              this.$store.state.currentTable.id,
              this.$store.state.currentTable.name
            )
        "
        class="title-box"
      >
        <h3 class="title">{{ this.shortTableTitle }}</h3>
        <pencil-icon class="title-edit-icon icon-2x" />
      </div>
    </div>
    <div class="add-column-btn col-10 col-xl-3 mx-auto" @click="showAddColumnModal">Create Column</div>
    <draggable v-model="columns">
      <transition-group type="transition" name="flip-list" class="columns">
        <column v-for="column in columns" v-bind:key="column.id" :column="column" class="column" />
      </transition-group>
    </draggable>
  </div>
</template>

<style lang="scss" scoped>
.flip-list-move {
  transition: transform 0.5s;
}

.title-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: 0 0 1.5rem 0;

  &:hover {
    cursor: pointer;
    color: #28a745;

    .title-edit-icon {
      color: #28a745;
    }
  }
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

  &:hover {
    background: rgb(212, 237, 218);
  }

  &:active {
    background: rgb(169, 220, 181);
  }
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
  width: 19.8rem;
}

@media only screen and (max-width: 640px) {
  .columns {
    flex-direction: column;
    justify-content: center;
  }

  .column {
    padding: 0 0 1.5rem 0;
    width: 80vw;
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
import DeleteColumn from '../components/modals/DeleteColumn.vue';
import RenameColumn from '../components/modals/RenameColumn.vue';
import AddEntry from '../components/modals/AddEntry.vue';
import DeleteEntry from '../components/modals/DeleteEntry.vue';

import { shorten } from '../util';

export default {
  name: 'Table',
  components: {
    Column,
    RenameTable,
    DeleteColumn,
    RenameColumn,
    AddEntry,
    AddColumn,
    DeleteEntry,
    draggable,
    PencilIcon,
  },
  computed: {
    shortTableTitle() {
      return shorten(this.$store.state.currentTable.name, 21);
    },
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
        tableId,
        tableName,
      });
    },
    showAddColumnModal() {
      this.$modal.show('add-column');
    },
  },
};
</script>
