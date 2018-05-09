def find_key(key, dictionary):
    """Returns values for all occurrances of the key provided.

    Arguments:
    key -- the key to search for.
    dictionary -- the dictionary to be searched.

    Return Value(s):
    Returns values in form of a generator.

    Exception(s):
    None

    Example: Get all occurances of matching key values
    dict_data = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True, 'etc': [{'one': True}]}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS', 'admin_url': '/my_account/admin/'}
    # as a generator...
    for x in find_key('models', dict_data):
        print(x)
    # or, using list comprehension...
    [print(x) for x in find_key('models', dict_data)]
    # or, as a list...
    l = list(find_key('admin_url', dict_data))

    Example: Get first occurance only using 'next()' function.
    # using 'None' as default value...
    v = next(find_key('models', dict_data), None)
    """
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find_key(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find_key(key, d):
                    yield result
