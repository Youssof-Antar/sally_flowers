/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

export class FlowerList extends Component {
    setup() {
        this.state = useState({
            flowers: [],
            newCommonName: "",
            newScientificName: "",
            newWateringFrequency: 3,
            newWateringAmount: 0,
            newSeasonStart: null,
            newSeasonEnd: null,
        });

        onMounted(() => this.loadFlowers());
    }

    async loadFlowers() {
        const products = await rpc("/web/dataset/call_kw", {
            model: "product.product",
            method: "search_read",
            args: [[["is_flower", "=", true]]],
            kwargs: {
                fields: [
                    "id",
                    "name",
                    "scientific_name",
                    "watering_frequency",
                    "watering_amount",
                    "season_start",
                    "season_end",
                ],
            },
        });

        this.state.flowers = products.map((p) => ({
            id: p.id,
            common_name: p.name, // map "name" → "common_name"
            scientific_name: p.scientific_name,
            watering_frequency: p.watering_frequency,
            watering_amount: p.watering_amount,
            season_start: p.season_start,
            season_end: p.season_end,
        }));
    }

    async addFlower() {
        if (!this.state.newCommonName.trim()) return;

        const flowerId = await rpc("/web/dataset/call_kw", {
            model: "product.product",
            method: "create",
            args: [
                {
                    name: this.state.newCommonName,
                    is_flower: true,
                    scientific_name: this.state.newScientificName,
                    watering_frequency: this.state.newWateringFrequency,
                    watering_amount: this.state.newWateringAmount,
                    season_start: this.state.newSeasonStart,
                    season_end: this.state.newSeasonEnd,
                },
            ],
            kwargs: {},
        });

        this.state.flowers.push({
            id: flowerId,
            common_name: this.state.newCommonName,
            scientific_name: this.state.newScientificName,
            watering_frequency: this.state.newWateringFrequency,
            watering_amount: this.state.newWateringAmount,
            season_start: this.state.newSeasonStart,
            season_end: this.state.newSeasonEnd,
        });

        // Reset
        this.state.newCommonName = "";
        this.state.newScientificName = "";
        this.state.newWateringFrequency = 3;
        this.state.newWateringAmount = 0;
        this.state.newSeasonStart = null;
        this.state.newSeasonEnd = null;
    }
}

FlowerList.template = "sally_flowers.FlowerList";
