<template>
  <div class="container">
    <div @click="onClickTitle" class="title">{{ shortTitle }}</div>
    <div @click="onClickDelete" class="icon">
      <close-icon />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;
}

.title {
  flex: 1 0 auto;
  line-height: 40px;
  user-select: none;
}

.icon {
  flex: 0 1 auto;
  display: flex;

  &:hover {
    color: brown;
  }
}
</style>

<script>
import CloseIcon from 'vue-material-design-icons/Close.vue';
import { shorten } from '../util';

export default {
  name: 'table-entry',
  components: {
    CloseIcon,
  },
  computed: {
    shortTitle() {
      return shorten(this.name, 31);
    },
  },
  props: ['name', 'id', 'onClickTitle', 'onClickDelete'],
};
</script>
