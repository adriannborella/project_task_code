# -*- coding: utf-8 -*-
from odoo import http

# class ProjectTaskCode(http.Controller):
#     @http.route('/project_task_code/project_task_code/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_task_code/project_task_code/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_task_code.listing', {
#             'root': '/project_task_code/project_task_code',
#             'objects': http.request.env['project_task_code.project_task_code'].search([]),
#         })

#     @http.route('/project_task_code/project_task_code/objects/<model("project_task_code.project_task_code"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_task_code.object', {
#             'object': obj
#         })