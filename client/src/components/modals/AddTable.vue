
<template>
  <modal
    name="add-table"
    transition="pop-out"
    :clickToClose="false"
    :adaptive="adaptive"
    :height="height"
    @opened="fixFocus"
    @closed="onClose"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Create a new table</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">Please enter a title for the new table:</label>
            <input
              id="title-form"
              class="form-control"
              v-model="table_name"
              placeholder="Title"
              ref="addTableInput"
            />
          </div>
        </div>
      </div>
      <div class="dialog-buttons">
        <button type="button" class="dialog-button" @click="createClick">CREATE</button>
        <button type="button" class="dialog-button" @click="closeModal">CANCEL</button>
      </div>
    </div>
  </modal>
</template>

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
      this.$modal.hide('add-table');
    },
    async createClick() {
      const order = this.$store.state.tables.length;
      this.createTable(this.table_name, order);
      this.$modal.hide('add-table');
    },
    fixFocus() {
      this.$refs.addTableInput.focus();
    },
    onClose() {
      this.table_name = '';
    },
  },
};
</script>
