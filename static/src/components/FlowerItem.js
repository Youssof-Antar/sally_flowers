/** @odoo-module **/
import { Component } from "@odoo/owl";

export class FlowerItem extends Component {
  static template = "sally_flowers.FlowerItem";
  static props = {
    flower: {
      type: Object,
      required: true, 
    },
  };
}
