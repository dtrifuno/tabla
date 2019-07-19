
<template>
  <modal
    name="add-column"
    transition="pop-out"
    :clickToClose="false"
    :adaptive="adaptive"
    :height="height"
    @closed="onClose"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">Create a new column</div>
        <div class="dialog-c-text">
          <div class="form-group">
            <label for="title-form">Title of new column</label>
            <input id="title-form" class="form-control" v-model="columnTitle" placeholder="Title" />
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
  },
};
</script>
