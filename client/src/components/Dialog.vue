
<template>
  <modal
    name="dialog"
    transition="pop-out"
    :adaptive="adaptive"
    :height="height"
    @before-open="beforeOpen"
  >
    <div class="dialog">
      <div class="dialog-content">
        <div class="dialog-title">{{this.title}}</div>
        <div class="dialog-c-text">{{this.body}}</div>
      </div>
      <div class="dialog-buttons">
        <button
          type="button"
          class="dialog-button"
          @click="this.confirmClick"
        >{{ this.confirmLabel }}</button>
        <button type="button" class="dialog-button" @click="this.closeModal">{{ this.cancelLabel }}</button>
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

.dialog-button {
  flex: 1 1 100%;
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
  name: 'delete-table',
  data() {
    return {
      tableName: '',
      tableId: '',
      adaptive: true,
      height: 'auto',
      modal: 0,
    };
  },
  methods: {
    ...mapActions(['removeTable']),
    beforeOpen(event) {
      this.title = event.params.title;
      this.body = event.params.body;
      this.confirmLabel = event.params.confirmLabel
        ? event.param.confirmLabel
        : 'YES';
      this.cancelLabel = event.params.cancelLabel
        ? event.params.cancelLabel
        : 'NO';
      this.confirmClick = event.params.confirmClick;
    },
    closeModal() {
      this.$modal.hide('delete-table');
    },
    async confirmClick() {
      console.log(this.tableId);
      this.removeTable(this.tableId);
      this.$modal.hide('delete-table');
    },
  },
};
</script>
