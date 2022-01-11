# Knowledge base entailment

def transformRule(rule):
  rule = rule.replace('~', ' not ')
  rule = rule.replace('^', ' and ')
  rule = rule.replace('v', ' or ')
  return rule

def checkEntailment(rule, query):
  possibilities = [
    (False, False, False),
    (False, False, True),
    (False, True, False),
    (False, True, True),
    (True, False, False),
    (True, False, True),
    (True, True, False),
    (True, True, True)
  ]

  rule = transformRule(rule)

  for P, Q, R in possibilities:
    p = str(P)
    q = str(Q)
    r = str(R)
    query = str(query)
    rule = rule.replace('P', p)
    rule = rule.replace('Q', q)
    rule = rule.replace('R', r)
    KB = eval(rule)
    query = eval(query)
    print('KB: {}, query: {}'.format(KB, query))
    if KB == True and query == False:
      print('KB does not entail query')
      return
  print('KB entails query')

def main():
  rule = '(~Qv~PvR)^(~Q^P)^Q'
  query = 'R'
  print('rule: {}, query: {}'.format(rule, query))
  checkEntailment(rule, query)

main()