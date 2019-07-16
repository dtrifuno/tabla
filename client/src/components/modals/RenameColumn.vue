
<template>
  <modal
    name="rename-column"
    transition="pop-out"
    :adaptive="adaptive"
    :height="height"
    @closed="onClose"
    @before-open="beforeOpen"
    @opened="fixFocus"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Rename column</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">
              Enter a new title for the column
              <b>{{this.columnName}}</b>:
            </label>
            <input
              id="title-form"
              class="form-control"
              v-model="newColumnName"
              placeholder="Title"
              ref="newColumnInput"
            />
          </div>
        </div>
      </div>
      <div class="dialog-buttons">
        <button type="button" class="dialog-button" @click="renameClick">RENAME</button>
        <button type="button" class="dialog-button" @click="closeModal">CANCEL</button>
      </div>
    </div>
  </modal>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'rename-column',
  data() {
    return {
      newColumnName: '',
      columnId: '',
      columnName: '',
      adaptive: true,
      height: 'auto',
    };
  },
  methods: {
    ...mapActions(['renameColumn']),
    closeModal() {
      this.$modal.hide('rename-column');
    },
    async renameClick() {
      await this.renameColumn({
        columnId: this.columnId,
        name: this.newColumnName,
      });
      this.$modal.hide('rename-column');
    },
    beforeOpen(event) {
      this.newColumnName = event.params.columnName;
      this.columnName = event.params.columnName;
      this.columnId = event.params.columnId;
    },
    onClose() {
      this.newColumnName = '';
    },
    fixFocus() {
      this.$refs.newColumnInput.focus();
    },
  },
};
</script>
