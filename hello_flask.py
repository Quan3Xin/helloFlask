from flask import Flask, render_template, request, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError  # 验证信息

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello flask'


class Name_Form(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired(message=u'内容不能不为空')],
                       # label='请输入用户名',
                       render_kw={
                           "required oninvalid": "setCustomValidity('请输入账号')",
                           "class": "control-label col",
                           "placeholder": "请输入你的名字",
                           "oninput": " setCustomValidity('')"
                       })
    submit = SubmitField('Submit',
                         render_kw={
                             "class": "btn btn-default"
                         })


@app.route('/', methods=['GET', 'POST'])
def index():
    form_tables = Name_Form()  # 实例化
    if form_tables.validate_on_submit():  # 判断submit
        data = form_tables.name.data  # 实例化 form_table.data

        print(data)
    return render_template('hello.html', form=form_tables)


if __name__ == '__main__':
    app.run(port=8991)
