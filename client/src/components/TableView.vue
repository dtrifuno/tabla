<template>
  <div class="table">
    <column v-for="(column, index) in columns" v-bind:column="column" v-bind:key="index"/>
    <router-link to="/table">Go home</router-link>
  </div>
</template>

<script>
import Column from "./Column";
export default {
  name: "TableView",
  components: { column: Column },
  data: function() {
    return {
      columns: [
        {
          title: "Friday (Morning)",
          color: "violet",
          entries: [
            {
              position: 0,
              title: "1. Write a thesis",
              description:
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse mattis vestibulum leo, non vestibulum felis."
            },
            {
              position: 2,
              title: "3. Write a thesis",
              description:
                "Curabitur sodales, lacus quis vehicula cursus, eros neque lacinia eros, quis rutrum magna felis sit amet tortor."
            },
            {
              position: 1,
              title: "2. Create a lootfilter",
              description:
                "Phasellus efficitur quam at ex vestibulum, nec consequat elit dictum. Vivamus dapibus mi eu arcu hendrerit, a pulvinar libero imperdiet."
            }
          ]
        },
        {
          title: "Sunday (Afternoon)",
          color: "azure",
          entries: [
            {
              position: 0,
              title: "Kill Shaper",
              description:
                "Aliquam elementum semper arcu, porttitor vehicula orci molestie id. Curabitur porttitor faucibus nibh, sed ullamcorper ante euismod non."
            }
          ]
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.table {
  display: flex;
  flex-direction: row;
}

.item-dropzone-area {
  color: green;
  width: 5rem;
  height: 1rem;
}
</style>
