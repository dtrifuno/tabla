<template>
  <modal
    name="delete-column"
    transition="pop-out"
    :adaptive="adaptive"
    :clickToClose="false"
    :height="height"
    @before-open="beforeOpen"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Delete a column</div>
        <div class="dialog-c-text">
          <p>
            Are you sure you want to delete the column
            <b>{{ this.column.name }}</b>
            ?
          </p>
          <p>This action will delete all entries in the column and cannot be undone.</p>
        </div>
      </div>
      <div class="dialog-buttons">
        <button type="button" class="dialog-button" @click="confirmClick">YES</button>
        <button type="button" class="dialog-button" @click="closeModal">NO</button>
      </div>
    </div>
  </modal>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'delete-column',
  data() {
    return {
      adaptive: true,
      column: {},
      height: 'auto',
    };
  },
  methods: {
    ...mapActions(['removeColumn']),
    beforeOpen(event) {
      this.column = event.params.column;
    },
    closeModal() {
      this.$modal.hide('delete-column');
    },
    async confirmClick() {
      this.removeColumn(this.column.id);
      this.$modal.hide('delete-column');
    },
  },
};
</script>
