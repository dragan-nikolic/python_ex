def demo_simple_format():
    name = "John"
    age = 30
    print(f'Name: {name} Age: {age}')

def demo_not_all_fields_provided(
        fstring,
        name,
        source,
        target):

    if '{source}' in fstring and '{target}' in fstring:
        print(fstring.format(name=name, source=source, target=target))
    else:
        print(fstring.format(name=name))


def demo_find_curly_braces():
    print('=== demo_find_curly_braces ===')
    query = 'select {column} from {table}'

    params = ['column', 'table', 'xyz']

    params_ph = [f'{{{p}}}' for p in params]

    for ph in params_ph:
        position = query.find(ph)
        if position != -1:
            print(f"placeholder {ph} found in text '{query}' at position {position}")
        else: 
            print(f"placeholder {ph} NOT found in text '{query}'")
    print('===')

def demo_replace_params():
    print('=== demo_replace+params ===')
    query = 'select {column} from {table} where {column}={column_value}'

    params = ['column', 'table', 'column_value']
    values = [
        ['brand_id', 'rest', 'sonic'],
        ['brand_id', 'location', 'bww'],
        ['rest_id', 'rest', '00583']
    ]

    params_ph = [f'{{{p}}}' for p in params]
    print(f'params_placeholders: {params_ph}')

    parametrized_queries = []

    for value in values:

        new_query = query
        for i in range(len(params)):
            new_query = new_query.replace(params_ph[i], value[i])

        parametrized_queries.append(new_query)

    print('--- parametrized queries ---')
    for query in set(parametrized_queries):
        print(f'query: {query}')

# ---- demos ----

# demo_simple_format()

# demo_not_all_fields_provided(
#     "Transferring {name} from {source} to {target}",
#     "file1.txt", 
#     "adls", 
#     "smb")

# demo_not_all_fields_provided(
#     "Transferring {name}",
#     "file1.txt", 
#     None, 
#     None)

demo_find_curly_braces()
demo_replace_params()