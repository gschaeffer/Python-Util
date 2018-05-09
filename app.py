from dictutil import find_key

example = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True, 'etc': [{'one': True}]}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS', 'admin_url': '/my_account/admin/'}

for x in find_key('models', example):
    print(x)

[print(x) for x in find_key('models', example)]

v = next(find_key('modelss', example), None)
print(v)
