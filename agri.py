from openerp.osv import fields, osv
import time
from openerp import netsvc
import datetime
import openerp.addons.decimal_precision as dp
import openerp.addons.extension_management 
from lxml import etree
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT

class land_category(osv.Model):
  _name = 'landcategory'
  _description = 'Land Categories'

  _columns = {
      'name': fields.char('Category Name', required=True, select=True),
      'parent_id': fields.many2one('landcategory','Parent Category', select=True, ondelete='cascade'),
      'child_id': fields.one2many('landcategory', 'parent_id', string='Child Categories'),
      }
land_category()


class agri_record(osv.Model):
    _name = 'agri.record'
    _description = 'Agriculture Management'
    _columns = {
        'pest_name': fields.char('Pest Name', required=True),
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        }

agri_record()

class weed_manag(osv.Model):
    _name = 'weed.manag'
    _description = 'Weed Management'
    _columns = {
        'weed_name': fields.char('Weed Name', required=True),
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        }

weed_manag()


class disease_manag(osv.Model):
    _name = 'disease.manag'
    _description = 'Disease Management'
    _columns = {
        'disease_name': fields.char('Disease Name', required=True),
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        'des' : fields.html('Description'),
        }

disease_manag()

class scouting(osv.Model):
    _name = 'scouting'
    _description = 'Scouting Management'
    _columns = {
        
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        'des' : fields.html('Description'),
        }

scouting()

class crop_irrigation(osv.Model):
    _name = 'crop.irrigation'
    _description = 'Crop Irrigation Management'
    _columns = {
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        'des' : fields.html('Description'),
        }

crop_irrigation()

class practice_package(osv.Model):
    _name = 'practice.package'
    _description = 'Package of practice'
    _columns = {
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        'des' : fields.html('Description'),
        }

practice_package()

class intercrop_practice(osv.Model):
    _name = 'intercrop.practice'
    _description = 'Intercropping practice'
    _columns = {
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        'des' : fields.html('Description'),
        }

intercrop_practice()


class field_operation(osv.Model):
    _name = 'field.operation'
    _description = 'Field Operation'
    _columns = {
        'type': fields.char('Type', size= 64, required= True),
        'corp': fields.char('Corp'),
        'des' : fields.html('Description'),
        }

field_operation()

class crops(osv.Model):
    _name = 'crops'
    _description = 'Crops'
    _columns = {
            'irrigation_line':fields.one2many('irrigation.details', 'irrigation'),
            'landpreparation_line':fields.one2many('landpreparation.details', 'landpreparation'),
            'fertilizer_line':fields.one2many('fertilizer.details', 'fertilizer'),
            'sowing_line':fields.one2many('sowing.details', 'sowing'),
            'sampling_line':fields.one2many('sampling.details', 'sampling'),
            'survey_line':fields.one2many('survey.details','survey'),
            'harvesting_line':fields.one2many('harvesting.details', 'harvesting'),
            'scouting_line':fields.one2many('scouting.details', 'scout'),
            'pest_line':fields.one2many('pest.issue', 'pest'),
            'weeding_line':fields.one2many('weeding.controle', 'weeding'),
            'disease_line':fields.one2many('disease.issue', 'disease'),
            'weed_line':fields.one2many('weed.issue', 'weed'),
            'insect_line':fields.one2many('insect.issue', 'insect'),
            'treat_line':fields.one2many('treat.issue', 'treat'),
            'crop_name':fields.char('Cultivation Name', size= 64, required= True),
            'land_name':fields.many2one('plot', 'Plot Name'),
            'type': fields.char('Crop Type', size= 64),
            'fert_used' : fields.char('Fertilizers Used', size=64),
            'sowing_date' : fields.datetime('Planting Date'),
            'harvesting_date' : fields.datetime('Harvesting Date'),
            'crop_variety' : fields.char('Crop Variety', size=64),
            'year' : fields.integer('Year of Cultivation',size=64),
            'current_crop' : fields.char('Current Crop',size=64),
            'crop_yield' : fields.integer('Yield', size=64),
            'des' : fields.html('Description'),
            'actual_productivity':fields.integer("Actual Productivity",size=64),
            'estimated_productivity' : fields.integer('Estimated Productivity',size=64),
            'state': fields.selection([('initial', 'Initial'), ('surveyed','Surveyed'), ('landprepared', 'Land Preparation'), ('planted', 'Planting'), ('intercropping', 'Intercropping'), ('harvest', 'Harvesting'), ('ratoon', 'Ratooning')],
            'Status', readonly=False, help='The status of the current cultivation', copy=False),
        }
crops()

class land_preparation(osv.osv):
    _name = "landpreparation.details"
    _description = "Land Preparation"
    _columns = {
      'landpreparation' : fields.many2one('crops', readonly=True),
            'land_preparation_date' : fields.datetime('Date', size=64),
            'activity' : fields.char('Activity',size=64 , required= True),
            'duration' : fields.integer('Duartion',size=64, required= True),
            'area_covered' : fields.char('Area Covered' , size=64, required= True),
    }
land_preparation()


class irrigation_details(osv.osv):
    _name = "irrigation.details"
    _description = "details of crop irrigation"
    _columns = {
              'irrigation':fields.many2one('crops', readonly=True),
              'irrigation_date': fields.datetime('Irrigation Date', size=64),
              'irrigation_type': fields.char('Type of Irrigation', size=64),
              'irrigation_source' : fields.char('Irrigation Source'),
        }
irrigation_details()


class fertilizer_details(osv.osv):
    _name = "fertilizer.details"
    _description = "details of Fertilizeres used"
    _columns = {
        'fertilizer':fields.many2one('crops', readonly=True),
        'use_date': fields.datetime('Use Date', size=64),
        'fertilizer_name': fields.char('Name of Fertilizer', size=64),
        'fertilizer_type': fields.char('Type of Fertilizer', size=64),
    }
fertilizer_details()

class sowing_details(osv.osv):
    _name = "sowing.details"
    _description = "Sowing Details"
    _columns = {
        'sowing':fields.many2one('crops', readonly=True),
        'date': fields.datetime('Date Of Sowing'),
        'seed_name': fields.char('Name of seed', size=64),
        'seed_type': fields.char('Quality of seed', size=64),
        }
sowing_details()

class harvesting_details(osv.osv):
    _name = "harvesting.details"
    _description = "Harvesting Details"
    _columns = {
          'harvesting':fields.many2one('crops', readonly=True),
          'start_date': fields.datetime('From '),
          'end_date': fields.datetime('To'),
          'amount': fields.integer('Amount', size=64),
          'type' : fields.selection([('mechanical', 'Mechanical'), ('manual', 'Manual')], 'Harvesting Type'),           
        }
harvesting_details()


class destructive_sampling(osv.osv):
    _name = "sampling.details"
    _description = 'Destructive Sampling'
    _columns = {
          'sampling':fields.many2one('crops', readonly=True),
          'date' : fields.datetime('Date'),
          'purity' : fields.char('Purity',size=64),
          'pole_percent' : fields.char('Pole %',size=64),
          'fiber_percent' : fields.char('Fiber %',size=64),
          'sample_size' : fields.char('Sample Size',size=64, readonly=True),
          'briks' : fields.char('Briks',size=64,readonly=True),
          'pole'  : fields.char('Pole',size=64,required=True),
    }  
destructive_sampling()


class hr_bricks_survey(osv.osv):
    _name = "survey.details"
    _description = 'Destructive Sampling'
    _columns = {
        'survey':fields.many2one('crops', readonly=True),
        'date' : fields.datetime('Date'),
        'middle'  : fields.char('Middle',size=64,required=True),
        'bottom' : fields.char('Bottom',size=64),
        'sample_size' : fields.char('Sample Size',size=64, readonly=True),
        'top' : fields.char('Top',size=64,readonly=True),
    }
hr_bricks_survey()


class scouting_details(osv.osv):
    _name = "scouting.details"
    _description = "Scouting Details"
    _columns = {
              'issue_line':fields.one2many('scouting.issue', 'issue'),
              'scout':fields.many2one('crops', readonly=True),
              'date': fields.datetime('Date Of Inspection'),
    }
scouting_details()

class scouting_issue(osv.osv):
    _name = "scouting.issue"
    _description = "Scouting Details"
    _columns = {
              'issue':fields.many2one('scouting.details', readonly=True),
              'new_issue': fields.html('Issue'),
    }
scouting_issue()


class weeding_controle(osv.osv):
    _name = "weeding.controle"
    _description = 'Weeding Controle'
    _columns = {
          'weeding':fields.many2one('crops', readonly=True),
          'date' : fields.datetime('Date'),
          'used_chemical'  : fields.char('Middle',size=64,required=True),
     }  
weeding_controle()

class pest_issue(osv.osv):
    _name = "pest.issue"
    _description = "Pest Details"
    _columns = {
              'pest':fields.many2one('crops', readonly=True),
              'pest_name': fields.char('Pest Name', size=64),
              'sevirity': fields.char('Savierity',size=64),
              'area' : fields.char('Area Affected'),
              'moniter_date':fields.datetime('Moniter Date'),
      }
pest_issue()

class disease_issue(osv.osv):
    _name = "disease.issue"
    _description = "disease Details"
    _columns = {
              'disease':fields.many2one('crops', readonly=True),
              'disease_name': fields.char('Disease Name', size=64),
              'sevirity': fields.char('Savierity',size=64),
              'area' : fields.char('Area Affected'),
              'moniter_date':fields.datetime('Moniter Date'),
             }
disease_issue()

class weed_issue(osv.osv):
    _name = "weed.issue"
    _description = "disease Details"
    _columns = {
              'weed':fields.many2one('crops', readonly=True),
              'weed_name': fields.char('weed Name', size=64),
              'area' : fields.char('Area Affected'),
              'moniter_date':fields.datetime('Moniter Date'),
             }
weed_issue()

class insect_issue(osv.osv):
    _name = "insect.issue"
    _description = "Insect Details"
    _columns = {
              'insect':fields.many2one('crops', readonly=True),
              'insect_name': fields.char('Insect Name', size=64),
              'area' : fields.char('Area Affected'),
              'sevirity': fields.char('Savierity',size=64),
              'moniter_date':fields.datetime('Moniter Date'),
              'ins_use':fields.char('Insectiside Used'),
             }
insect_issue()

class treat_issue(osv.osv):
    _name = "treat.issue"
    _description = "Treatment Details"
    _columns = {
      'treat':fields.many2one('crops', readonly=True),
      'date':fields.datetime('Date of Treatment'),
      'pest_use': fields.char('Pestiside Used'),          
      'ins_use':fields.char('Insectiside Used'),
      'fungi_use':fields.char('Fungiside Used'),
      'type' : fields.selection([('incetiside','Incetiside'),('prestiside','Prestiside')],'Type'),
      'quantity' : fields.char('Amount',size=60), 
    }
treat_issue()

class plot(osv.Model):
    _name = 'plot'
    _description = 'plot'
    _columns = {
        'soil_line':fields.one2many('soil.details', 'soil'),
        'cultivation_line':fields.one2many('cultivation.history', 'history'),
        'plot_name':fields.char('Plot Name', size= 64),
        'plot_number':fields.integer('Plot Number', size= 64, required= True),
        'area': fields.integer('Area of land', size= 64, required= True),
        'location': fields.char('Location', size= 64, required= True),
        'gis': fields.char('GIS Coordinates', size= 64, required= True),
        'des' : fields.html('Description'),
        "land_category_id" :  fields.many2one('landcategory','Categories'),
    }
plot()

class soil_details(osv.osv):
    _name = "soil.details"
    _description = "Soil Details"
    _columns = {
        'soil':fields.many2one('plot', readonly=True),
        'type':fields.char('Soil Type'),
        'ph': fields.char('Soil PH'),          
        'color':fields.char('Color of Soil'),
        'npk':fields.char('NPK percentage'),
    }
soil_details()

class cultivation_history(osv.osv):
    _name = "cultivation.history"
    _description = "Cultivation History Details"
    _columns = {
      'history':fields.many2one('plot', readonly=True),
      'c_name':fields.char('Name of Crop'),
      'start_date': fields.datetime('Start Date'),          
      'end_date':fields.datetime('End Date'),
      'production': fields.integer('Production in KG'),
    }
cultivation_history()

class seed_verity(osv.Model):
  _name = "seed.verity"
  _description = "Seed Verity"
  _columns = {
      'name' : fields.char('Verity Name'),
      'seed_kg' : fields.integer('Number of Seed Per Kg'),
  }
seed_verity()






