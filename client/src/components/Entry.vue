<template>
  <div class="container">
    <div class="edit-click">
      <drag-variant-icon class="icon" />
      <div class="title">{{ this.name }}</div>
    </div>
    <div class="delete-click" @click="this.onClickDelete">
      <close-icon class="delete-icon icon" />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  display: flex;
  background-color: white;
  min-height: 2.5rem;
  width: 100%;
  flex-direction: row;
  border: 0.5px solid rgba(0, 0, 0, 0.125);
  padding: 0.5rem 0.35rem;

  &:hover {
    background-color: rgb(252, 252, 252);
  }

  &:active {
    background-color: rgb(248, 248, 248);
  }
}

.title {
  flex: 1 0 auto;
  text-align: left;
  display: block;
  width: 70%;
  padding: 0 0.2rem 0 0.5rem;
}

.delete-click {
  display: flex;
  align-content: center;
  cursor: pointer;

  &:hover .delete-icon {
    color: brown;
  }
}

.edit-click {
  display: flex;
  flex-direction: row;
  align-items: center;
  flex: 1 0 auto;
  width: 90%;
  cursor: pointer;

  &:hover .edit-icon {
    color: #28a745;
  }
}
</style>

<script>
import CloseIcon from 'vue-material-design-icons/Close.vue';
import DragVariantIcon from 'vue-material-design-icons/DragVariant.vue';

export default {
  name: 'entry',
  components: {
    CloseIcon,
    DragVariantIcon,
  },
  props: ['name', 'id', 'onClickTitle', 'onClickDelete'],
};
</script>
