from flask import Flask, render_template, redirect, flash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.user import User
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
import logging

from models.register import RegisterForm

# 设置日志级别
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')  # 输出到控制台，设置格式

app = Flask(__name__)
bootstrap = Bootstrap(app)

# set optional bootswatch theme
# 设置Flask_admin样式
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'Iamasecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost:3306/datagen'

# 初始化admin对象，绑定app对象，指定模板
admin = Admin(app, name='microblog', template_mode='bootstrap3')

# 数据库连接
engine = create_engine(config.DB_URI)
session = Session(engine)
# 创建数据库管理对象
db = SQLAlchemy(app)

# Add administrative views here
admin.add_view(ModelView(User, session))

# 菜单栏格式
# 如果某个菜单栏有多个子目录，则使用Subgroup代替View
nav = Nav()
nav.register_element('top', Navbar(u'数寻平台',
                                   View(u'主页', 'index'),
                                   View(u'数据源', 'about'),
                                   View(u'数据查询', 'about'),
                                   View(u'数据生成', 'about'),
                                   View(u'注册', 'register'),
                                   # Subgroup(u'数据生成',
                                   #          View(u'Mysql', 'about'),
                                   #          Separator(),
                                   #          View(u'Oracle', 'service'),
                                   #          Separator(),
                                   #          View(u'Postgresql', 'service'),
                                   #          Separator(),
                                   #          View(u'Mongodb', 'service'),
                                   #          ),
                                   ))
# 这里的View指定route的函数名
nav.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", title_name='Welcome')


@app.route("/<name>")
def home(name):
    return render_template("home.html", name=name)


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.route('/service')
def service():
    return 'service'


@app.route('/about')
def about():
    return 'about'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    logging.info("form validate: %s" % form.validate())
    logging.info("form request method: %s" % request.method)
    if request.method == 'POST' and form.validate():
        logging.info(1)
        user = User(form.username.data, form.email.data, form.password.data)
        logging.info(2)
        session.add(user)
        logging.info(3)
        session.commit()
        logging.info(4)
        flash('注册成功，感谢。')
        return redirect(url_for("login"))
    else:
        flash("注册失败。")
        logging.warning("注意：注册表单数据输入不正确：用户名：%s，邮箱：%s，密码：%s" % (
            form.username.data, form.email.data, form.password.data))
    return render_template("/user/register.html", form=form, title_name="数寻平台-注册")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("/user/login.html", title_name="数寻平台-登录")

