
<template>
  <modal
    name="rename-column"
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
        <div class="dialog-title">Rename column</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">
              Enter a new title for the column
              <b>{{this.column.name}}</b>:
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
      column: {},
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
        id: this.column.id,
        name: this.newColumnName,
        prev: this.column.prev,
      });
      this.$modal.hide('rename-column');
    },
    beforeOpen(event) {
      this.newColumnName = event.params.column.name;
      this.column = event.params.column;
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
