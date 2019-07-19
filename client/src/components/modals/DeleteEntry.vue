
<template>
  <modal
    name="delete-entry"
    transition="pop-out"
    :adaptive="adaptive"
    :clickToClose="false"
    :height="height"
    @before-open="beforeOpen"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Delete an entry</div>
        <div class="dialog-c-text">
          <p>Are you sure you want to delete the entry:</p>
          <p>
            <b>{{this.entry.name}}</b>
          </p>
          <p>This action cannot be undone.</p>
        </div>
      </div>
      <div class="dialog-buttons">
        <button type="button" class="dialog-button" style="flex: 1 1 100%" @click="confirmClick">YES</button>
        <button type="button" class="dialog-button" style="flex: 1 1 100%" @click="closeModal">NO</button>
      </div>
    </div>
  </modal>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'delete-entry',
  data() {
    return {
      adaptive: true,
      entry: {},
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['removeEntry']),
    beforeOpen(event) {
      this.entry = event.params.entry;
      this.columnId = event.params.columnId;
    },
    closeModal() {
      this.$modal.hide('delete-entry');
    },
    async confirmClick() {
      this.removeEntry({ entry: this.entry, columnId: this.columnId });
      this.$modal.hide('delete-entry');
    },
  },
};
</script>
