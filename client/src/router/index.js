import Vue from "vue";

import Router from "vue-router";

import HelloWorld from "@/components/HelloWorld";
import TableView from "@/components/TableView";

//import "vue-material-design-icons/styles.css";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "TableView",
      component: TableView
    },
    {
      path: "/table",
      name: "HelloWorld",
      component: HelloWorld
    }
  ]
});
