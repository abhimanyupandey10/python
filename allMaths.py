a = 2
b = 4
c = 8

print ('Default order:' , a, '*' , c,'+', b,'=', a * (c+b))
print ('Forced order:' , a, '* (',c,'+', b,') =', a * (c+b))

print ('Default order:' , c, '//' , b,'-', a, '=', c // (b-a))
print ('Forced order:' , c, '// (',b,'-', a,') =', c // (b-a))

print ('Default order:' , c, '%' , a,'+', b, '=', c + (a+b))
print ('Forced order:' , c, '% (',a,'+', b,') =', c + (a+b))

print ('Default order:' , c, '**' , a,'+', b, '=', c ** (a+b))
print ('Forced order:' , c, '** (',a,'+', b,') =', c ** (a+b))