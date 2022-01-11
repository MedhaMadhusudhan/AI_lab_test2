# steps to convert fol to cnf
# eliminate biconditionals and implications
# move ! inwards
# each quantifier should use a different variable
# skolemization
# drop universal quantifiers
# distribute V over ^

import string

def implication(clause):
  if '=>' in clause:
    vals = clause.split('=>')
    lhs = implication(vals[0])
    rhs = implication(vals[1])
    print(lhs, rhs)
    return '!({})V{}'.format(lhs, rhs)
  else:
    return clause

def complement(clause):
  all_clauses = [val for val in clause.split('V')]

  for i in range(len(all_clauses)):
    if all_clauses[i][0] == '!':
      rem_clause = all_clauses[i][2: len(all_clauses[i])-1]
      changed_quantifiers = ''
      for j in range(len(rem_clause)):
        if rem_clause[j] == '∀':
          changed_quantifiers += '∃'
        elif rem_clause[j] == '∃':
          changed_quantifiers += '∀'
        elif rem_clause[j] == '^':
          changed_quantifiers += 'V'
        elif rem_clause[j] == 'V':
          changed_quantifiers += '^'
        elif rem_clause[j] in string.ascii_uppercase and rem_clause[j] != 'V':
          changed_quantifiers += '~' + rem_clause[j]
        else:
          changed_quantifiers += rem_clause[j]

      all_clauses[i] = changed_quantifiers

  return ' V '.join(all_clauses)

def skolemize(clause):
  if '∃' in clause:
    new_clause = clause[clause.index(' ')+1:]
    new_clause = new_clause.replace('x', 'const')
    return new_clause
  return clause 

def main():
  fol_statement = '∀x King(x) ^ Greedy(x) => Evil(x)'
  res_clause = fol_statement

  if '=>' in res_clause:
    res_clause = implication(res_clause)
    print(res_clause)
  
  if '!' in res_clause:
    res_clause = complement(res_clause)
    print(res_clause)
  
  res_clause = skolemize(res_clause)
  print(res_clause)
  
main()