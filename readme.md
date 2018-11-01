flask db init来创建microblog的迁移存储库：


不会对数据库进行任何更改，只会生成迁移脚本
flask db migrate -m "users table"

upgrade()函数应用迁移，downgrade()函数回滚迁移

更新到最新版本
flask db upgrade


回滚上次的迁移
flask db downgrade

导入Flask
export FLASK_APP=blog.py


export FLASK_DEBUG=1

HTML<form>元素被用作Web表单的容器。 表单的action属性告诉浏览器在提交用户在表单中输入的信息时应该请求的URL
action设置为空字符串时，表单将被提交给当前地址栏中的URL

form.hidden_tag()模板参数生成了一个隐藏字段

消息flash
get_flashed_messages

filter_by()的结果是一个只包含具有匹配用户名的对象的查询结果集


