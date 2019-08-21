import multiprocessing

bind = "127.0.0.1:9000"   #绑定的ip与端口
workers = 2                #核心数
errorlog = '/home/xxx/xxx/gunicorn.error.log' #发生错误时log的路径
accesslog = '/home/xxx/xxx/gunicorn.access.log' #正常时的log路径
#loglevel = 'debug'   #日志等级
proc_name = 'gunicorn_project'   #进程名