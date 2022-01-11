# main function
# Knowledge base dictionary
# unification
# forward chaining
def main():
  KB = [
    'American(x)^Weapon(y)^Sells(x,y,z)^Hostile(z)=>Criminal(x)',
    'Owns(Nono,M1)',
    'Missile(M1)',
    'Missile(x)^Owns(Nono,x)=>Sells(West,x,Nono)',
    'Missile(x)=>Weapon(x)',
    'Enemy(x,America)=>Hostile(x)',
    'American(West)',
    'Enemy(Nono,America)'
  ]

  #print(KB)

  KB_unified = len(KB)*[False]
  final_state = len(KB)*[True]
  
  base_conditions = []
  print('step 1:')
  for i in range(len(KB)):
    if '=>' not in KB[i] and not KB_unified[i]:
      print(KB[i])
      KB_unified[i] = True
      base_conditions.append(KB[i])
 
  step = 2
  while KB_unified != final_state:
    print('\nstep {} :'.format(step))
    for i in range(len(KB)):
      if not KB_unified[i]:
        vals = KB[i].split('=>')
        lhs = vals[0].split('^')
        rhs = vals[1]
        
        lhs_predicates = [ele[:ele.index('(')] for ele in lhs]
        base_predicates = [ele[:ele.index('(')] for ele in base_conditions]
        rhs_vars = rhs[rhs.index('(')+1: rhs.index(')')].split(',')
       
        if set(lhs_predicates).issubset(set(base_predicates)):
          for j in range(len(lhs_predicates)):
            pred_vars = lhs[j][lhs[j].index('(')+1: lhs[j].index(')')].split(',')
            predicate_index = base_predicates.index(lhs_predicates[j])
            lhs[j] = base_conditions[predicate_index]
            pred_var_replacements = lhs[j][lhs[j].index('(')+1: lhs[j].index(')')].split(',')
            for k in range(len(pred_vars)):
              if pred_vars[k] in rhs_vars and len(pred_vars[k]) == 1:
                rhs_vars[rhs_vars.index(pred_vars[k])] = pred_var_replacements[k]
            
          rhs_unified = rhs[:rhs.index('(')+1] + ','.join(rhs_vars) + ')'
          lhs_unified = ' ^ '.join(lhs)
          print('{} => {}'.format(lhs_unified, rhs_unified))
          base_conditions.append(rhs_unified)
          KB_unified[i] = True
    step += 1

main()