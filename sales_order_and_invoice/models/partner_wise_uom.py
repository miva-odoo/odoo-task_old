# -*- coding: utf-8 -*-

from odoo import fields,models

class PartnerWiseUom(models.Model):
	_name = 'partner.wise.uom'


	#----------------------------
    #  fields Declaration
    #---------------------------

	partner_id = fields.Many2one('res.partner',default=lambda self: self.uid)
	product_id = fields.Many2one('product.product')
	uom_id = fields.Many2one('uom.uom')
	category_uom_ids = fields.Many2one(related="product_id.uom_id.category_id")
	uom_ids = fields.Many2one('uom.uom' , string='uom' , domain="[('category_id','=', category_uom_ids)]")

