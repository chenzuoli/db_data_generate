# coding=utf-8
from urllib.parse import urljoin

import markupsafe
from flask_admin.contrib.fileadmin import FileAdmin
from werkzeug.utils import secure_filename
from wtforms import form, fields, validators
from sqlalchemy.orm import registry
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from flask_admin.contrib.sqla import ModelView

my_registry = registry()
Base = my_registry.generate_base()


# 增加数据库模型视图
# 定义数据表
class DataOrigin(Base):
    __tablename__ = "connections"

    conn_id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    table_type = Column(String(50), nullable=False)
    url = Column(String(100))
    username = Column(String(100))
    _password_hash = Column(String(200))
    host = Column(String(50))
    port = Column(String(10))
    db = Column(String(20))
    param = Column(String(100))
    driver_jar = Column(String(100))


# 定义数据表单
class DataOriginForm(form.Form):
    """
    表单限制条件
    不能为空：[validators.DataRequired()]
    可以为空：[validators.Optional()]
    描述：description
    默认值：default
    选择框：choice
    强制类型转换：coerce
    注意：如果表单中某个字段为FileField，则界面会出现【选择文件】界面
        SelectField为下拉选择界面
        StringField为文本输入界面
    """

    table_type = fields.SelectField('数据库类型', [validators.InputRequired()], coerce=int,
                                    choices=[(1, 'mysql'), (2, 'oracle'), (3, 'postgresql')])
    url = fields.StringField("数据库连接串", validators=[validators.DataRequired()])
    username = fields.StringField('数据库用户名', [validators.DataRequired()])
    _password_hash = fields.StringField('数据库密码', [validators.Optional()], default='dfjoief23jlfs',
                                        description='编辑时输入则表示修改密码，不修改用户密码则不要修改任何数据')
    host = fields.StringField('数据库ip地址', [validators.Optional()], default='localhost',
                              description="如果【数据库连接串】中包含了host，则此处可以不填写")
    port = fields.IntegerField('数据库端口', [validators.Optional()],
                               description='如果【数据库连接串】中包含了端口，则此处可以不填写')
    db = fields.StringField('数据库', [validators.Optional()], default='default',
                            description="如果【数据库连接串】中包含了数据库，则此处可以不填写")
    param = fields.StringField('连接参数', [validators.Optional()],
                               description='数据库连接参数')
    driver_jar = fields.FileField('驱动jar包', [validators.DataRequired()],
                                  description='jdbc驱动，需上传对应jar包')


# 定义数据模型
class DataOriginView(ModelView):
    # 通过Model和Form分别制定数据库表模型和表单模型
    model = DataOrigin
    form = DataOriginForm

    # can_create-允许新建、can_edit-允许修改、can_delete-允许删除、can_view_details-允许查看明细
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    details_modal = True
    can_export = True

    # column_list-显示字段、column_details_list-显示明细字段
    # column_labels-字典，以字符形式显示相关字段、column_formatters-字段格式化
    column_list = ['table_type', 'url', 'host', 'port']
    column_details_list = ['conn_id', 'table_type', 'url', 'host', 'port', 'username', 'db', 'param', 'created_at',
                           'updated_at']
    column_labels = dict(
        conn_id='连接id', table_type='数据库类型', url='连接串', host='数据库ip地址', port='数据库端口',
        username='数据库用户名', db='数据库', param='连接参数', created_at='创建时间', updated_at='更新时间',
    )

    def format_image(view, context, model, name):
        """用户头像设置的是FileField，其在界面是一个文件选择，需要将其转换成上传后的文件url地址"""
        _value = getattr(model, name, None)  # getattr() 函数用于返回一个对象属性值
        img_src = urljoin("static/img", _value) if _value else '#'
        _value = markupsafe.Markup('<img src="{}" width="100px"/>'.format(img_src))
        print(_value)
        return _value

    column_formatters = dict(
        status=lambda v, c, m, n: '正常' if m.status == 0 else '禁用',
        avatar=format_image  # 字段格式化方法
    )

    # 列过滤器
    column_filters = ('table_type', 'username', 'db')
    """更多内容可以查看flask_admin得model：https://flask-admin.readthedocs.io/en/latest/api/mod_model/"""


class MyFileAdmin(FileAdmin):
    """flask_admin实现文件上传功能，重写FileAdmin类"""
    md5_dir = ("images", "files")
    # can_upload、can_download、can_delete、can_delete_dirs、can_mkdir、can_rename
    can_delete = False
    can_rename = False
    # 允许上传文件的类型，类似的还有editable_extensions
    allowed_extensions = ("jpg", "png", "jpeg", "md", "tar")

    def _save_form_files(self, directory, path, form):
        print('存储文件~~~~')
        filename = self._separator.join([directory, secure_filename(form.upload.data.filename)])

        if self.storage.path_exists(filename):
            secure_name = self._separator.join([path, secure_filename(form.upload.data.filename)])
            print('文件已经存在')
            raise
        else:
            self.save_file(filename, form.upload.data)
            self.on_file_upload(directory, path, filename)
