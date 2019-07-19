<template>
  <modal
    name="add-column"
    transition="pop-out"
    :clickToClose="false"
    :adaptive="adaptive"
    :height="height"
    @closed="onClose"
    @opened="fixFocus"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Create a new column</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">Title of new column</label>
            <input
              id="title-form"
              class="form-control"
              v-model="columnTitle"
              placeholder="Title"
              ref="newColumnInput"
              @keyup.enter="triggerCreate"
            />
          </div>
        </div>
      </div>
      <div class="dialog-buttons">
        <button
          type="button"
          class="dialog-button"
          @click="createClick"
          ref="createColumnButton"
        >CREATE</button>
        <button type="button" class="dialog-button" @click="closeModal">CANCEL</button>
      </div>
    </div>
  </modal>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'AddColumn',
  data() {
    return {
      columnTitle: '',
      adaptive: true,
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['createColumn']),
    triggerCreate(event) {
      event.stopPropagation();
      this.$refs.createColumnButton.click();
    },
    closeModal() {
      this.$modal.hide('add-column');
    },
    createClick() {
      this.createColumn(this.columnTitle);
      this.$modal.hide('add-column');
    },
    onClose() {
      this.columnTitle = '';
    },
    fixFocus() {
      this.$refs.newColumnInput.focus();
    },
  },
};
</script>
