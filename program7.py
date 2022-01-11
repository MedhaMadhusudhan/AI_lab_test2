# function implication
# function bidirectional
# function complement
# function resolve
# main 

import string

def implication(clause):
  ele = clause.split('=>')
  lhs = ele[0]
  rhs = ele[1]
  return '{}V{}'.format(complement(lhs), rhs)
  
def bidirectional(clause):
  ele = clause.split('<=>')
  lhs = ele[0]
  rhs = ele[1]
  return '{}V{}'.format(complement(lhs), rhs), '{}V{}'.format(complement(rhs), lhs)

def complement(clause):
  if clause in string.ascii_uppercase:
    return clause.lower()
  else:
    return clause.upper()

def makeClauses(KB):
  clauses = []
  for ele in KB:
    if '^' in ele:
      vals = ele.split('^')
      lhs = vals[0]
      rhs = vals[1]
      clauses += makeClauses(lhs)
      clauses += makeClauses(rhs)
    elif '!' in ele:
      val = ele[1:]
      clauses += makeClauses(complement(val))
    elif '=>' in ele:
      clauses.append(implication(ele))
    elif '<=>' in ele:
      ele1, ele2 = bidirectional(ele)
      clauses.append(ele1)
      clauses.append(ele2)
    else:
      clauses.append(ele)
  return clauses

def simplify(clause1, clause2):
  variables = [c for c in clause1 if c in string.ascii_letters and c!= 'V']
  variables += [c for c in clause2 if c in string.ascii_letters and c != 'V']
  variables = list(set(variables))
  for var in variables:
    if var in string.ascii_uppercase and var.lower() in variables:
      variables.remove(var)
      variables.remove(var.lower())
  #print('V'.join(variables))
  return 'V'.join(variables)

def resolve(KB, alpha):
  clauses = makeClauses(KB)
  clauses += complement(alpha)
  print('clauses are as follows: ', clauses)
  for clause1 in clauses:
    for clause2 in clauses:
      if clause1 != clause2:
        result = simplify(clause1, clause2)
        #print('{} + {} = {}'.format(clause1, clause2, result))
        if result == '':
          print('KB entails alpha')
          return
        if result not in clauses:
          clauses.append(result)
  print('KB does not entail alpha')

def main():
  KB = ['a=>b', 'b=>c', '!c']
  alpha = 'A'
  resolve(KB, alpha)

main()