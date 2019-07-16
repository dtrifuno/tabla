
<template>
  <modal
    name="delete-column"
    transition="pop-out"
    :adaptive="adaptive"
    :height="height"
    @before-open="beforeOpen"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Delete a column</div>
        <div class="dialog-c-text">
          <p>
            Are you sure you want to delete the column
            <b>{{this.columnName}}</b>?
          </p>
          <p>This action will delete all entries in the column and cannot be undone.</p>
        </div>
      </div>
      <div class="dialog-buttons">
        <button type="button" class="dialog-button" style="flex: 1 1 100%" @click="confirmClick">YES</button>
        <button type="button" class="dialog-button" style="flex: 1 1 100%" @click="closeModal">NO</button>
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
      columnId: '',
      columnName: '',
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['removeColumn']),
    beforeOpen(event) {
      this.columnId = event.params.columnId;
      this.columnName = event.params.columnName;
    },
    closeModal() {
      this.$modal.hide('delete-column');
    },
    async confirmClick() {
      this.removeColumn(this.columnId);
      this.$modal.hide('delete-column');
    },
  },
};
</script>
