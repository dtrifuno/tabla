<template>
  <div class="container">
    <div @click="onClickTitle" class="title">{{ this.name }}</div>
    <div @click="onClickDelete" class="icon">
      <close-icon />
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
}

.title {
  flex: 1 0 auto;
  line-height: 40px;
}

.icon {
  flex: 0 1 auto;
  padding: 2.5%;
}

.icon:hover {
  color: brown;
}
</style>

<script>
import CloseIcon from 'vue-material-design-icons/Close';

export default {
  name: 'table-entry',
  components: {
    CloseIcon,
  },
  props: ['name', 'id', 'onClickTitle', 'onClickDelete'],
};
</script>
