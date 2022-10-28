from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.user import User
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
bootstrap = Bootstrap(app)

# set optional bootswatch theme
# 设置Flask_admin样式
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'Iamasecretkey'

# 初始化admin对象，绑定app对象，指定模板
admin = Admin(app, name='microblog', template_mode='bootstrap3')

# 数据库连接
engine = create_engine(config.DB_URI)
session = Session(engine)

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


if __name__ == '__main__':
    app.run(debug=True)
