
<template>
  <modal name="add-table" transition="pop-out" :adaptive="adaptive" :height="height">
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Create a new table</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">Please enter a title for the new table:</label>
            <input id="title-form" class="form-control" v-model="table_name" placeholder="Title" />
          </div>
        </div>
      </div>
      <div class="dialog-buttons">
        <button
          type="button"
          class="dialog-button"
          style="flex: 1 1 100%"
          @click="createClick"
        >CREATE</button>
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
  name: 'AddTable',
  data() {
    return {
      table_name: '',
      adaptive: true,
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['createTable']),
    closeModal() {
      this.table_name = '';
      this.$modal.hide('add-table');
    },
    async createClick() {
      await this.createTable(this.table_name);
      this.table_name = '';
      this.$modal.hide('add-table');
    },
  },
};
</script>
