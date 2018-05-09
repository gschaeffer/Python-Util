from dictutil import find_key
import json

example = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True, 'etc': [{'one': True}]}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS', 'admin_url': '/my_account/admin/'}

with open("event.json", "r") as f:
  data = f.read()
example = json.loads(data)

for x in find_key('accountId', example):
    print(x)

[print(x) for x in find_key('accountId', example)]

v = next(find_key('accountId', example), None)
print(v)
