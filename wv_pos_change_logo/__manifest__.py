{
    'name': "POS Change Logo",
    'version': '1',
    'summary': """
        This module help us to show custom Logo on the POS session.

        """,
    'author': 'WebVeer',
    'category': 'Point Of Sale',
    
    'website': '',

    'depends': ['point_of_sale'],
    'data': [
            'pos.xml'
        ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'images': ['static/description/selected.png'],
    'price': 5.00,
    'currency': 'EUR',
    'installable': True,
}
