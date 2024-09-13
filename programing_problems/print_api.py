# Task: Parse the given input list of strings and output them formatted as shown below

# Input
routes = [
    '/home',
    '/account/account',
    '/account/payments',
    '/account/payments/details',
    '/subscriptions/details',
    '/subscriptions/status',
]

parsed_routes = {
    'home': {},
    'account': {
        'account': {},
        'payments': {
            'details': {}
        },
    },
    'subscription:': {
        'status': {},
        'details': {}
    }
}

# Output Structure
#
# - home
# - account
#     - account
#     - payments
#         - details
# - subscriptions
#     - details
#     - status

routes = [
    '/home',
    '/account/account',
    '/account/payments',
    '/account/payments/details',
    '/subscriptions/details',
    '/subscriptions/status',
]


def merge_nested_dict(dict1, dict2):
    for key, value in dict2.items():
        if dict1.get(key):
            merge_nested_dict(dict1[key], dict2[key])
        else:
            dict1[key] = value
            return


def get_routes_dict(indent=4, prefix='- ', level=0):
    routes_dict = {}
    for route in routes:
        paths = route.lstrip('/').split('/')
        path_dict = get_path_dict(paths)
        merge_nested_dict(routes_dict, path_dict)

    return routes_dict


def get_path_dict(paths):
    path_dict = {}
    for path in paths:
        if len(paths) == 1:
            return {paths[0]: {}}
        else:
            path_dict[paths[0]] = get_path_dict(paths[1:])

    return path_dict


def print_path_dict(path_dict, indent=4, prefix='- ', level=0):
    for key, val in path_dict.items():
        print_path(key, indent=indent, prefix=prefix, level=level)
        if val:
            print_path_dict(val, indent=indent, prefix=prefix, level=level+1)


def print_path(pathname, indent=4, prefix='- ', level=0):
    print("{}{}{}".format(' ' * level * indent, prefix, pathname))


print_path_dict(get_routes_dict())
