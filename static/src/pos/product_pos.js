import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";

patch(ProductScreen.prototype, {
  get products() {
    const { limit_categories, iface_available_categ_ids } = this.pos.config;
    if (limit_categories && iface_available_categ_ids.length > 0) {
      const productIds = new Set([]);
      for (const categ of iface_available_categ_ids) {
        const categoryProducts = this.getProductsByCategory(categ);
        for (const p of categoryProducts) {
          productIds.add(p.id);
        }
      }
      return this.pos.models["product.product"].filter((p) =>
        productIds.has(p.id)
      );
    }
    return this.pos.models["product.product"].filter(
      (p) => p.is_flower == true
    );
  },
});
