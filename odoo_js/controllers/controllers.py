# -*- coding: utf-8 -*-
# from odoo import http


# class OdooJs(http.Controller):
#     @http.route('/odoo_js/odoo_js', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_js/odoo_js/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_js.listing', {
#             'root': '/odoo_js/odoo_js',
#             'objects': http.request.env['odoo_js.odoo_js'].search([]),
#         })

#     @http.route('/odoo_js/odoo_js/objects/<model("odoo_js.odoo_js"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_js.object', {
#             'object': obj
#         })
