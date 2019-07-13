<template>
  <div class="container">
    <div class="edit-click">
      <drag-variant-icon class="icon" />
      <div @click="onClickTitle" class="title">{{ this.name }}</div>
      <pencil-icon class="edit-icon icon" />
    </div>
    <div class="delete-click">
      <close-icon class="delete-icon icon" />
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  max-width: 20vw;
  min-height: 2.5rem;
  flex-direction: row;
  border: 0.5px solid rgba(0, 0, 0, 0.125);
  padding: 0.25rem 0.25rem;
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
}

.delete-click:hover .delete-icon {
  color: brown;
}

.edit-click {
  display: flex;
  flex-direction: row;
  align-items: center;
  flex: 1 0 auto;
  width: 90%;
  cursor: pointer;
}

.edit-click:hover .edit-icon {
  color: green;
}

.icon:hover {
  color: brown;
}
</style>

<script>
import CloseIcon from 'vue-material-design-icons/Close.vue';
import PencilIcon from 'vue-material-design-icons/Pencil.vue';
import DragVariantIcon from 'vue-material-design-icons/DragVariant.vue';

export default {
  name: 'entry',
  components: {
    CloseIcon,
    PencilIcon,
    DragVariantIcon,
  },
  props: ['name', 'id', 'onClickTitle', 'onClickDelete'],
};
</script>
