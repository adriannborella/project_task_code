# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    sequence_task_id = fields.Many2one(
        string='Sequencia de las tareas',
        comodel_name='ir.sequence',
        ondelete='restrict',
    )
    
    code = fields.Char(
        string='Code',
    )

    def create_sequence(self):
        new_sequence = self.env['ir.sequence'].create({
            'name' : f'Sequence {self.name}',
            'prefix' : self.code if self.code != False else self.name[0:2],
            'padding' : 4,
            'number_next_actual' : 1
        })
        self.write({ 'sequence_task_id': new_sequence.id })

    def get_next_code(self):
        # import ipdb; ipdb.set_trace()
        if not (self.sequence_task_id):
            self.create_sequence()
        
        result = self.sequence_task_id.get_next_char(self.sequence_task_id.number_next_actual)
        self.sequence_task_id.number_next_actual += 1
        return result
    
    def generate_task_code(self):
        tasks = self.task_ids.search([('project_id','=', self.id),('code','=', False)])
        for record in tasks:
            record.code = self.get_next_code()
    
class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    @api.multi
    @api.depends('name', 'code')
    def name_get(self):
        result = []
        for record in self:
            if record.code:
                name = '[' + record.code + '] ' + record.name
            else:
                name = record.name
            result.append((record.id, name))
        return result
    
    
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        import ipdb; ipdb.set_trace()
        domain = []
        if name:
            domain = [
                '|','|','|', ('name', '=ilike', name), ('name', operator, name),
                ('code', '=ilike', name), ('code', operator, name)
            ]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&', '!'] + domain[1:]
        records = self.search(domain + args, limit=limit)
        return records.name_get()
    
    code = fields.Char(
        string='Code',
    )

    @api.model
    def create(self, vals):
        result =  super(ProjectTask, self).create(vals)
        if(result.project_id):
            result.code = result.project_id.get_next_code()
        
        return result