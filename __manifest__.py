{
    "name": "Sally Flowers",
    "version": "1.0",
    "summary": "Manage Sally’s flower shop",
    "category": "Custom",
    "author": "You",
    "depends": ["base", "web", "product", "point_of_sale"],
    "assets": {
        "web.assets_backend": [
            "sally_flowers/static/src/**/*.js",
            "sally_flowers/static/src/**/*.xml",

        ],
        'point_of_sale._assets_pos': [
            "sally_flowers/static/src/**/*.xml",
            "sally_flowers/static/src/**/*.js",
        ],
    },
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
         "views/product_views.xml",
    ],
    "installable": True,
    "application": True,
}
