
<template>
  <modal name="rename-table" transition="pop-out" :adaptive="adaptive" :height="height">
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Rename table</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">
              Enter a new title for the table
              <b>{{this.$store.state.currentTable.name}}</b>:
            </label>
            <input id="title-form" class="form-control" v-model="newTableName" placeholder="Title" />
          </div>
        </div>
      </div>
      <div class="dialog-buttons">
        <button
          type="button"
          class="dialog-button"
          style="flex: 1 1 100%"
          @click="renameClick"
        >RENAME</button>
        <button
          type="button"
          class="dialog-button"
          style="flex: 1 1 100%"
          @click="closeModal"
        >CANCEL</button>
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
  name: 'RenameTable',
  data() {
    return {
      newTableName: '',
      adaptive: true,
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['renameCurrentTable', 'fetchTables']),
    closeModal() {
      this.newTableName = '';
      this.$modal.hide('rename-table');
    },
    async renameClick() {
      await this.renameCurrentTable(this.newTableName).then(() => {
        this.fetchTables();
      });
      this.newTableName = '';
      this.$modal.hide('rename-table');
    },
  },
};
</script>
