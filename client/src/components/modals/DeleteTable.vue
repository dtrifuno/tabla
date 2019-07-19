
<template>
  <modal
    name="delete-table"
    transition="pop-out"
    :adaptive="adaptive"
    :clickToClose="false"
    :height="height"
    @before-open="beforeOpen"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Delete a table</div>
        <div class="dialog-c-text">
          <p>
            Are you sure you want to delete the table
            <b>{{this.tableName}}</b>?
          </p>
          <p>This action will delete all entries in the table and cannot be undone.</p>
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
  name: 'delete-table',
  data() {
    return {
      adaptive: true,
      height: 'auto',
      tableId: '',
      tableName: '',
    };
  },
  methods: {
    ...mapActions(['removeTable']),
    beforeOpen(event) {
      this.tableId = event.params.tableId;
      this.tableName = event.params.tableName;
    },
    closeModal() {
      this.$modal.hide('delete-table');
    },
    async confirmClick() {
      this.removeTable(this.tableId);
      this.$modal.hide('delete-table');
    },
  },
};
</script>
