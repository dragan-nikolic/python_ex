string_with_params = 'adding {} and {} you get {}'
print(string_with_params.format(2, 3, 5))

fstring_with_params = f'adding {{}} and {{}} you get {{}}'
print(fstring_with_params.format(3, 5, 8))

num1 = 5
num2 = 8
result = 13
fstring_with_embbeded_variables = f'adding {num1} and {num2} you get {result}'
print(fstring_with_embbeded_variables)

string_with_named_params = 'adding {num1} and {num2} you get {result}'
print(string_with_named_params.format(num1=8, num2=13, result=21))  
print(string_with_named_params.format(num2=21, result=34, num1=13))  # named params can be in any order 

fstring_with_named_params = f'adding {{num1}} and {{num2}} you get {{result}}'
print(fstring_with_named_params.format(num2=34, result=55, num1=21))  # named params can be in any order 

docstring_with_params = """
    SELECT {}
    FROM {};
"""
print(docstring_with_params.format('brand_id', 'comp_sales'))

docstring_with_named_params = '''
    SELECT {field}
    FROM {table};
'''
print(docstring_with_named_params.format(field='rest_id', table='cmx_data'))

mytable = 'daily_sales'
fdocstring_with_named_params_and_embedded_vars = f'''
    SELECT {{field}}
    FROM {mytable};
    WHERE {{field}} IS NOT NULL 
'''
print(fdocstring_with_named_params_and_embedded_vars.format(field='location_id'))
