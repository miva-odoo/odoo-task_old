# -*- coding: utf-8 -*-

from odoo import fields,models


class ResPartner(models.Model):
    _inherit='res.partner'

    #----------------------------
    #  fields Declaration
    #---------------------------

    partner_wise_uoms_id = fields.One2many('partner.wise.uom','partner_id', )
    # current_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.partner_wise_uoms_id, readonly=True)




	
    
   

    



    

    
