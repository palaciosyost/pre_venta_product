{
    'name': 'Fecha de publicacion de preventa productos - orden de compra - E-commerce',
    'version': '1.0',
    'description': 'Gestionar las fecha de preventa de los productos con estados y fechas de entrada de los produtos segun la fecha de entreha de las ordenes de entrega haciendo la publicacion de los productos en el e-cpmmerce',
    'summary': '',
    'author': 'F.P.C. Technology',
    'website': 'https://fpc_technology.com',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base', 'purchase', 'website', 'web'
    ],
    'data': [
        'view/view_product_template.xml',
        "view/view_purchrse_order.xml",
        "view/web/view_web_product.xml",
        "view/action_server.xml",
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        "web.assets_frontend" : [
            "pre_venta_product/static/src/product.js"
        ]
    }
}