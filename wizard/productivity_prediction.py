from openerp.osv import fields, osv

class productivity_prediction_wizard(osv.osv_memory):
  _name = "productivity.prediction"
  _description = 'Productivity Prediction'
  _columns = {
      'plot_id': fields.many2one('plot', 'Select Farm'),
      'plant_per_acre' : fields.integer('Plant per Acre', size=64),
      'state': fields.selection([('step1', 'step1'),('step2', 'step2')])  
  }
  def action_next(self, cr, uid, ids, context=None):
      #your treatment to click  button next 
      #...
      # update state to  step2
      self.write(cr, uid, ids, {'state': 'step2',}, context=context)
      #return view
      return {
            'name' : 'Estimation of Plants Per Acre',
            'type': 'ir.actions.act_window',
            'res_model': 'plant.estimation',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': 'view_plant_estimation_wizard',
            'views': [(False, 'form')],
            'target': 'new',
             }

class plant_estimation(osv.osv_memory):
  _name = "plant.estimation"
  _description = 'Plant Per Acre'
  _columns = {
      'location1': fields.integer("Location1",size=64),
      'location2': fields.integer("Location2",size=64),
      'location3': fields.integer("Location3",size=64),
      'location4': fields.integer("Location4",size=64),
      'location5': fields.integer("Location5",size=64),
      'location6': fields.integer("Location6",size=64),
      'location7': fields.integer("Location7",size=64),
      'location8': fields.integer("Location8",size=64),
      'location9': fields.integer("Location9",size=64),
      'location10': fields.integer("Location10",size=64),
  }
  def action_next(self, cr, uid, ids, context=None):
      #your treatment to click  button next 
      #...
      # update state to  step2
      self.write(cr, uid, ids, {'state': 'step2',}, context=context)
      #return view
      return {
            'name' : 'Estimation of Pods Per Plant',
            'type': 'ir.actions.act_window',
            'res_model': 'pods.estimation',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': 'view_pods_estimation_wizard',
            'views': [(False, 'form')],
            'target': 'new',
      }
 

class pods_estimation(osv.osv_memory):
  _name = "pods.estimation"
  _description = 'Pods Estimation'
  _columns = {
      'location1': fields.integer("Location1",size=64),
      'location2': fields.integer("Location2",size=64),
      'location3': fields.integer("Location3",size=64),
      'location4': fields.integer("Location4",size=64),
      'location5': fields.integer("Location5",size=64),
      'location6': fields.integer("Location6",size=64),
      'location7': fields.integer("Location7",size=64),
      'location8': fields.integer("Location8",size=64),
      'location9': fields.integer("Location9",size=64),
      'location10': fields.integer("Location10",size=64),
  }
  def action_next(self, cr, uid, ids, context=None):
      #your treatment to click  button next 
      #...
      # update state to  step2
      self.write(cr, uid, ids, {'state': 'step2',}, context=context)
      #return view
      return {
            'name' : 'Estimation of Seed Per Pod',
            'type': 'ir.actions.act_window',
            'res_model': 'seed.estimation',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': 'view_seed_estimation_wizard',
            'views': [(False, 'form')],
            'target': 'new',
      }
 

class seed_estimation(osv.osv_memory):
  _name = "seed.estimation"
  _description = 'Seed Estimation Per pod'
  _columns = {
      'location1': fields.integer("Location1",size=64),
      'location2': fields.integer("Location2",size=64),
      'location3': fields.integer("Location3",size=64),
      'location4': fields.integer("Location4",size=64),
      'location5': fields.integer("Location5",size=64),
      'location6': fields.integer("Location6",size=64),
      'location7': fields.integer("Location7",size=64),
      'location8': fields.integer("Location8",size=64),
      'location9': fields.integer("Location9",size=64),
      'location10': fields.integer("Location10",size=64),
  }
  def action_next(self, cr, uid, ids, context=None):
      #your treatment to click  button next 
      #...
      # update state to  step2
      self.write(cr, uid, ids, {'state': 'step2',}, context=context)
      #return view
      return {
            'name' : "Seed Verity",
            'type': 'ir.actions.act_window',
            'res_model': 'seed.estimation_kg',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': 'view_seed_estimation_kg_wizard',
            'views': [(False, 'form')],
            'target': 'new',
      }
class seed_estimation_kg(osv.osv_memory):
  _name = "seed.estimation_kg"
  _description = 'Seed Estimation Per Kg'
  _columns = {
        'seed_verity_id': fields.many2one('seed.verity',"Seed Verity"),
        'seed_kg' : fields.integer("Seed Per Kg"),
  }
  def onchange_seed_verity_id(self, cr, uid, ids, seed_verity_id, context=None):
        value = {'seed_kg': False}
        if seed_verity_id:
            seed_verity = self.pool.get('seed.verity').browse(cr, uid, seed_verity_id)
            value['seed_kg'] = seed_verity.seed_kg
        return {'value': value}
 

   


