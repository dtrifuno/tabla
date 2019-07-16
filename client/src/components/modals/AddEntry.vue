
<template>
  <modal
    name="add-entry"
    transition="pop-out"
    :adaptive="adaptive"
    :height="height"
    @before-open="beforeOpen"
    @opened="fixFocus"
    @closed="onClose"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Add entry</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form"></label>
            <input
              id="title-form"
              class="form-control"
              v-model="entryContent"
              placeholder="Entry"
              ref="newEntryInput"
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
  name: 'AddEntry',
  data() {
    return {
      entryContent: '',
      adaptive: true,
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['createEntry']),
    closeModal() {
      this.$modal.hide('add-entry');
    },
    createClick() {
      this.createEntry({ columnId: this.columnId, name: this.entryContent });
      this.$modal.hide('add-entry');
    },
    onClose() {
      this.entryContent = '';
    },
    beforeOpen(event) {
      this.columnId = event.params.columnId;
    },
    fixFocus() {
      this.$refs.newEntryInput.focus();
    },
  },
};
</script>
