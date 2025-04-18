# 2024 Moval Agroingeniería
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Forestry Association Management',
    'summary': 'In a forestry association, management of owners and parcels.',
    'version': '16.0.1.0.0',
    'category': 'Forestry Associations',
    'website': 'https://www.moval.es',
    'author': 'Moval Agroingeniería',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'post_init_hook': 'post_init_hook',
    'depends': [
        'base_ter',
    ],
    'data': [
        'views/base_ter_menus.xml',
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'base_foa/static/src/scss/base_foa.scss',
            ('remove', 'base_ter/static/lib/ter_iconset/iconset.css'),
            'base_foa/static/lib/ter_iconset/iconset.css',
        ],
        'web.assets_frontend': [
            ('remove', 'base_ter/static/lib/ter_iconset/iconset.css'),
            'base_foa/static/lib/ter_iconset/iconset.css',
        ],
        'web.report_assets_common': [
            ('remove', 'base_ter/static/lib/ter_iconset/iconset.css'),
            'base_foa/static/lib/ter_iconset/iconset.css',
        ],
    },
}
