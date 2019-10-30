from django.http import JsonResponse


class HttpCode:
    """
    定义状态码
    """
    ok = 200  # 正常请求
    params_error = 400  # 参数错误
    un_ath = 401  # 没有授权
    not_found = 404  # 请求资源错误
    method_error = 405  # 请求方法错误
    server_error = 500  # 服务器内部错误


def result(code=HttpCode.ok, message='', data=None, kwargs=None):
    """
    :param code:     状态码
    :param message:  返回消息
    :param data:     数据
    :param kwargs:   其他参数
    :return:
    """
    json_dict = {'code': code, 'message': message, 'data': data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        # 判断kwargs是否有值，更新到字典中
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


def ok():
    """
    正常请求
    :return:
    """
    return result()


def params_error(message='', data=None):
    """
    参数错误
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.params_error, message=message, data=data)


def un_auth(message='', data=None):
    """
    没有授权
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.un_ath, message=message, data=data)


def not_found(message='', data=None):
    """
    请求资源不存在
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.not_found, message=message, data=data)


def method_error(message='', data=None):
    """
    请求方法错误
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.method_error, message=message, data=data)


def server_error(message='', data=None):
    """
    服务器错误
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.server_error, message=message, data=data)
