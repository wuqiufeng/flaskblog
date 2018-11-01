import os
basedir = os.path.abspath(os.path.dirname(__file__))

# uuid.uuid4().hex

class Config(object):
    # 密钥，用于生成签名或令牌 CSRF攻击 Cross-Site Request Forgery
    SECRET_KEY = os.environ.get('SECRET_KEY') or '983d97ae9d7f436db25ba2dff64d328e'

    # 获取应用的数据库的位置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # 设置数据发生变更之后是否发送信号给应用
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.163.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = True
    MAIL_USE_TSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'rootfuhz@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Fuhz1125430765'
    ADMINS = ['rootfuhz@163.com', 'rootfuhongzhu@163.com']

    POSTS_PER_PAGE = 2