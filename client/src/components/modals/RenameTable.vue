<template>
  <modal
    name="rename-table"
    transition="pop-out"
    :adaptive="adaptive"
    :clickToClose="false"
    :height="height"
    @closed="onClose"
    @before-open="beforeOpen"
    @opened="fixFocus"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Rename table</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">
              Enter a new title for the table
              <b>{{ this.tableName }}</b>
              :
            </label>
            <input
              id="title-form"
              class="form-control"
              v-model="newTableName"
              placeholder="Title"
              ref="renameTableInput"
              @keyup.enter="triggerRename"
            />
          </div>
        </div>
      </div>
      <div class="dialog-buttons">
        <button
          type="button"
          class="dialog-button"
          @click="renameClick"
          ref="renameTableButton"
        >RENAME</button>
        <button type="button" class="dialog-button" @click="closeModal">CANCEL</button>
      </div>
    </div>
  </modal>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'rename-table',
  data() {
    return {
      newTableName: '',
      tableName: '',
      tableId: '',
      adaptive: true,
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['renameCurrentTable', 'fetchTables']),
    triggerRename(event) {
      event.stopPropagation();
      this.$refs.renameTableButton.click();
    },
    closeModal() {
      this.$modal.hide('rename-table');
    },
    async renameClick() {
      await this.renameCurrentTable(this.newTableName).then(() => {
        this.fetchTables();
      });
      this.$modal.hide('rename-table');
    },
    beforeOpen(event) {
      this.newTableName = event.params.tableName;
      this.tableName = event.params.tableName;
      this.tableId = event.params.tableId;
    },
    onClose() {
      this.newTableName = '';
    },
    fixFocus() {
      this.$refs.renameTableInput.focus();
    },
  },
};
</script>
