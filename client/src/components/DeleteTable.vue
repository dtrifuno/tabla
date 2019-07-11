
<template>
  <modal
    name="delete-table"
    transition="pop-out"
    :adaptive="adaptive"
    :height="height"
    @before-open="beforeOpen"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Delete a table</div>
        <div
          class="dialog-c-text"
        >Are you sure you want to delete table "{{this.tableName}}"? This operation is not reversible.</div>
      </div>
      <div class="dialog-buttons">
        <button type="button" class="dialog-button" style="flex: 1 1 100%" @click="confirmClick">YES</button>
        <button type="button" class="dialog-button" style="flex: 1 1 100%" @click="closeModal">NO</button>
      </div>
    </div>
  </modal>
</template>

<style scoped>
.dialog {
  height: 100%;
  display: flex;
  flex-direction: column;
}
.dialog-content {
  flex: 1 0 auto;
  width: 100%;
  padding: 15px;
  font-size: 14px;
}

.dialog-buttons {
  display: flex;
  flex: 0 1 auto;
  width: 100%;
  border-top: 1px solid #eee;
}

.dialog-title {
  font-weight: 600;
  padding-bottom: 15px;
}

.dialog-button {
  font-size: 12px !important;
  background: transparent;
  outline: none;
  padding: 0;
  margin: 0;
  border: 0;

  box-sizing: border-box;
  line-height: 40px;
  height: 40px;
}

.dialog-button:hover {
  background: rgba(0, 0, 0, 0.01);
}

.dialog-button:active {
  background: rgba(0, 0, 0, 0.025);
}

.dialog-button:not(:first-of-type) {
  border-left: 1px solid #eee;
}
</style>


<script>
import { mapActions } from 'vuex';

export default {
  name: 'delete-table',
  data() {
    return {
      tableName: '',
      tableId: '',
      adaptive: true,
      height: 'auto',
      modal: 0,
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
      console.log(this.tableId);
      this.removeTable(this.tableId);
      this.$modal.hide('delete-table');
    },
  },
};
</script>
