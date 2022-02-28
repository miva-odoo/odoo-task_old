{
#imfromation
    
 'name':'Product Sale',
 'version': '15.0',
 'summary': 'Product Sale',
 'description': 'Product Sale',
 'category': 'custom',

# Author
 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['contacts','sale_management'],
 'data': [
     'views/res_partner_view.xml',
     'security/ir.model.access.csv',
     
 ],

 # Other
 'installable': True,
 'auto_install': False,
}