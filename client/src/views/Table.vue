<template>
  <div class="about">
    <add-column />
    <ul class="columns">
      <li>
        <ul class="column">
          <li class="column-header">Column 1 Heading</li>
          <li class="column-entry">First Title</li>
          <li class="column-entry">Second Title</li>
          <li class="column-entry">Third Title</li>
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
    </ul>
  </div>
</template>

<style scoped>
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
  border: 1px solid rgba(0, 0, 0, 0.125);
  font-weight: 800;
  background: rgba(0, 0, 0, 0.05);
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
</style>


<script>
import { mapActions } from 'vuex';

import { getTable } from '../api';
import AddColumn from '../components/AddColumn';

export default {
  name: 'Table',
  components: { AddColumn },
  methods: {
    showAddColumnModal() {
      this.$modal.show('add-column', {
        height: 'auto',
      });
    },
  },
};
</script>
