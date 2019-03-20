<template>
  <div class="container">
    <div class="column" v-bind:style="borderStyle">
      <h1 v-bind:style="headerStyle">{{column.title}}</h1>
      <ul>
        <draggable :list="column.entries" group="entries">
          <entry v-for="(entry, index) in column.entries" v-bind:key="index" v-bind:entry="entry"/>
        </draggable>
        <li class="addEntry" v-bind:style="addEntryStyle">
          <PlusIcon v-bind:size="32"/>
        </li>
      </ul>
      <div style="text-align: right;">
        <DeleteIcon/>
        <PencilIcon/>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";

import PlusIcon from "vue-material-design-icons/Plus.vue";
import PencilIcon from "vue-material-design-icons/Pencil.vue";
import DeleteIcon from "vue-material-design-icons/DeleteForever.vue";

import Entry from "./Entry";

export default {
  name: "Column",
  props: ["column"],
  components: { Entry, PlusIcon, PencilIcon, DeleteIcon, draggable },
  computed: {
    addEntryStyle: function() {
      return {
        order: Math.max(...this.column.entries.map(entry => entry.position)) + 1
      };
    },
    borderStyle: function() {
      return {
        border: `2px solid var(--${this.column.color})`
      };
    },
    headerStyle: function() {
      return {
        "background-color": `var(--${this.column.color})`
      };
    }
  }
};
</script>



<style lang="scss" scoped>
.container {
  width: 20rem;
  max-width: 90%;
  margin: 0;
  padding: 0.25rem;
}

.column {
  border: 1px solid black;
  margin: 0.25rem;
}

h1 {
  text-align: center;
  font-size: 1.4rem;
  margin: 0;
  padding: 0.6rem;
  background: red;

  color: white;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
}

.addEntry {
  border: 1px solid lightgrey;
  background-color: #ebebeb;
  margin: 0.5rem;
  padding: 0rem;
  cursor: pointer;
  transition: 0.3s;

  &:hover {
    background-color: lightgrey;
  }
}
</style>