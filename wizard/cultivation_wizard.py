from openerp.osv import fields, osv

class land_prepration_wizard(osv.osv_memory):
	_name = "land.preparation"
	_description = 'Land Preparation'
	_columns = {
		'crop_id': fields.many2one('crops', 'Cultivation Name'),
		'land_preparation_date' : fields.datetime('Date', size=64),
        'activity' : fields.char('Activity',size=64 , required= True),
        'duration' : fields.integer('Duartion',size=64, required= True),
        'area_covered' : fields.char('Area Covered' , size=64, required= True),	
	}
	def button_confirm(self,cr,uid,ids=False, context=None):
		self.write(cr, uid, ids, {'state':'confirm'})
	

class planting_wizard(osv.osv_memory):
	_name = "planting"
	_description = 'Planting'
	_columns = {
		'planting_date' : fields.datetime('Date',size=64 ),
		'variety' : fields.char('Variety',size=64 , required= True),
		'seed_quantity' : fields.char('Seed Quantity',size=64 , required= True),
		'fertilizer_quantity' : fields.char('Fertilizer Quantity',size=64 , required= True),
	}

class harvesting_wizard(osv.osv_memory):
	_name = "harvesting"
	_description = "Harvesting"
	_columns = {
			'type' : fields.selection([('fresh_cane','Fresh Cane'),('burnt_cane','Burnt Cane')],'Type'),
			'harvesting_date' : fields.datetime('Date', size=64),
			'yield' : fields.char('Yield' , size=64),
	}