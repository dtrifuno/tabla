<template>
  <li v-bind:style="{order: entry.position}">
    <div class="entry">
      <div class="entry-header" v-on:click="open ^= true">
        <h1>{{entry.title}}</h1>
        <ChevronDownIcon
          class="chevron"
          v-bind:class="{chevronUp: open, chevronDown: !open}"
          v-bind:size="36"
        />
      </div>
      <collapse-transition>
        <div class="entry-accordion" v-show="open">
          <div class="entry-description">{{entry.description}}</div>
          <div class="entry-footer">
            <div class="entry-icon">
              <PencilIcon v-bind:size="28"/>
            </div>
            <div class="entry-icon">
              <CursorMoveIcon v-bind:size="28"/>
            </div>
            <div class="entry-icon">
              <DeleteIcon v-bind:size="28"/>
            </div>
          </div>
        </div>
      </collapse-transition>
    </div>
  </li>
</template>

<script>
import ChevronDownIcon from "vue-material-design-icons/ChevronDown.vue";
import PencilIcon from "vue-material-design-icons/Pencil.vue";
import CursorMoveIcon from "vue-material-design-icons/CursorMove.vue";
import DeleteIcon from "vue-material-design-icons/DeleteForever.vue";

import { CollapseTransition } from "vue2-transitions";

export default {
  name: "Entry",
  props: ["entry"],
  components: {
    ChevronDownIcon,
    PencilIcon,
    DeleteIcon,
    CursorMoveIcon,
    CollapseTransition
  },
  data: function() {
    return {
      open: false
    };
  }
};
</script>

<style lang="scss" scoped>
.entry {
  padding: 0.1rem;
  border: 1px solid lightgrey;
  margin: 0.5rem;
}

.entry-header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  user-select: none;
}

.entry-accordion {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.entry-description {
  user-select: none;
  text-align: initial;
  padding: 0.25rem;
  width: 90%;
}

.entry-icon {
  border: 1px solid transparent;
  padding: 0.1rem 0.2rem;
  margin: 0 0.2rem;
  cursor: pointer;
  transition: 0.3s;

  &:hover {
    background-color: #ececec;
  }
}

.entry-footer {
  padding-top: 0.3rem;
  padding-bottom: 0.2rem;
  user-select: none;
  width: 100%;
  display: flex;
  justify-content: center;
}

h1 {
  font-size: 1.25rem;
  text-emphasis: none;
  margin: 0;
  text-align: left;
  font-weight: 400;
}

.chevronUp {
  animation: rotationUp 0.25s 1 ease-in normal forwards;
}

@keyframes rotationUp {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(180deg);
  }
}

.chevronDown {
  animation: rotationDown 0.25s 1 ease-in normal forwards;
}

@keyframes rotationDown {
  from {
    transform: rotate(180deg);
  }
  to {
    transform: rotate(0deg);
  }
}
</style>


