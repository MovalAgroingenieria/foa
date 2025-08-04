# 2024 Moval Agroingeniería
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, SUPERUSER_ID, exceptions, _


def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    incompatible_modules = ['base_wua', 'base_pdo', 'base_agf']
    installed_incompatible_modules = env['ir.module.module'].search([
        ('name', 'in', incompatible_modules), ('state', '=', 'installed')])
    if (installed_incompatible_modules and
       len(installed_incompatible_modules) > 0):
        raise exceptions.ValidationError(_(
            'Cannot install, incompatible modules are installed: %s.') % (
            ', '.join(installed_incompatible_modules.mapped('name'))))


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Load i18n_extra.
    env.ref('base.module_base_foa')._update_translations(
        overwrite=True)
