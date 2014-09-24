from openerp.osv import fields, osv
from openerp.tools.translate import _

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
      'total_avg' : fields.integer("Total Avg",readonly=True),
      'plant_population':fields.integer("Plant Population Per Acre",readonly=True),
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
  def first_change(self, cr, uid, ids,first1,first2,first3,first4,first5,first6,first7,first8,first9,first10 ,context=None):

    r=first1+first2+first3+first4+first5+first6+first7+first8+first9+first10
    r = r/10
    x = r*1000
    return {'value':{'total_avg':r,'plant_population':x}}
 

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
      'total_avg' : fields.integer("Total Avg",readonly=True),
      'pods_plant':fields.integer("Pods Per Plant",readonly=True),
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
  def first_change(self, cr, uid, ids,first1,first2,first3,first4,first5,first6,first7,first8,first9,first10 ,context=None):

    r=first1+first2+first3+first4+first5+first6+first7+first8+first9+first10
    r = r/10
    x = r
    return {'value':{'total_avg':r,'pods_plant':x}}

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
      'total_avg' : fields.integer("Total Avg",readonly=True),
      'seed_pod':fields.integer("Seed Per Pod",readonly=True),
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
  def first_change(self, cr, uid, ids,first1,first2,first3,first4,first5,first6,first7,first8,first9,first10 ,context=None):

    r=first1+first2+first3+first4+first5+first6+first7+first8+first9+first10
    r = r/10
    x = r
    return {'value':{'total_avg':r,'seed_pod':x}}


class seed_estimation_kg(osv.osv_memory):
  _name = "seed.estimation_kg"
  _description = 'Seed Estimation Per Kg'
  _inherit='seed.estimation'
  _columns = {
        'seed_verity_id': fields.many2one('seed.verity',"Seed Verity"),
        'seed_kg' : fields.integer("Seed Per Kg"),
        'yield': fields.integer('Yield Per Acre', size=56,readonly=True),
  }
  def action_next(self, cr, uid, ids, location1 , context=None):
      #your treatment to click  button next 
      #...
      # update state to  step2
      self.write(cr, uid, ids, {'seed_kg': '1234'}, context=context)
      #return view
      return {
            'name' : "Prediction Result",
            'type': 'ir.actions.act_window',
            'res_model': 'prediction.result',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': 'view_prediction_result_wizard',
            'views': [(False, 'form')],
            'target': 'new',
      }
  def onchange_seed_verity_id(self, cr, uid, ids, seed_verity_id,seed_pod, context=None):
        value = {'seed_kg': False}
        if seed_verity_id:
            seed_verity = self.pool.get('seed.verity').browse(cr, uid, seed_verity_id)
            value['seed_kg'] = seed_verity.seed_kg
            seed_pod1 = self.pool.get('seed.estimation').read(cr, uid,ids,['seed_pod'])
            print seed_po
            r = seed_pod1 + 10
            value['yield'] = r
        return {'value': value}



   


