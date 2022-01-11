# unification program

def Unify(expr1, expr2):
  predicate1 = predicate2 = None
  const1 = const2 = None
  args1 = args2 = None
  var1 = var2 = None
  temp = None

  if len(expr1) == 1:
    var1 = expr1
    
  if len(expr2) == 1:
    var2 = expr2
    
  if len(expr1) > 1:
    if '(' in expr1:
      predicate1 = expr1[:expr1.index('(')]
      temp = expr1[expr1.index('(')+1 : expr1.index(')')]
      args1 = temp.split(',')
      print('expr1 -> predicate : {}, arguments: {}'.format(predicate1, args1))
      
    else:
      const1 = expr1
    
  if len(expr2) > 1:
    if '(' in expr2:
      predicate2 = expr2[:expr2.index('(')]
      temp = expr2[expr2.index('(')+1 : expr2.index(')')]
      args2 = temp.split(',')
      print('expr2 -> predicate : {}, arguments: {}'.format(predicate2, args2))
      
    else:
      const2 = expr2
      
  if var1 != None and var2 != None:
    if var1 == var2:
      return '{}/{}'.format(var1, var2)
    else:
      return 'failure'
  elif var1 != None and const2 != None:
    return '{}/{}'.format(var1, const2)

  elif var2 != None and const1 != None:
    return '{}/{}'.format(var2, const1)

  elif const1 != None and const2 != None:
    if const1 == const2:
      return '{}/{}'.format(const1, const2)
    else:
      return 'failure'

  elif predicate1 != None and predicate2 != None and predicate1 != predicate2:
    return 'failure'

  elif predicate1 != None and predicate2 != None and predicate1 == predicate2 and len(args1) != len(args2):
    return 'failure'
    
  else:
    subst = ''
    result = None
    for i in range(len(args1)):
      result = Unify(args1[i], args2[i])
      if result == 'failure':
        return 'failure'
      else:
        for ele in result.split('/'):
          if len(ele) == 1 and ele in subst:
            return 'failure'
        if len(subst) == 0:
          subst += result
        else:
          subst = subst + ' , ' + result
    return subst
  

def main():
  expr1 = input('enter expr 1:  ')
  expr2 = input('enter expr 2:  ')

  print('\nresult: ',Unify(expr1, expr2))

main()