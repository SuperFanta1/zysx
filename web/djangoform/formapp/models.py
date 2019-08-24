from django.db import models

# 这个文件是用来创建数据模型的文件。
# Django后台框架对数据的增删改查操作，不是通过sql语句实现的，而是通过ORM的形式实现数据的增删改查操作。
# ORM: 对象关系映射。这种方式是通过类和对象的形式实现数据的增删改查操作，那么操作数据库就像在操作类和对象。
# ORM的优势：1.写法简单，抛弃复杂的sql语句；2.防止sql注入；

# python manage.py makemigrations: 负责收集models.py文件中数据模型的变化，如果这里的文件内容没有发生任何变化，会提示：No changes detected
# python manage.py migrate：将数据模型生成为数据库中的表。


class People(models.Model):
    """
    这里的类就代表了数据库中的表，想要创建表，定义一个类即可。
    """
    # 这里的类属性就代表了表中的字段，该字段是字符串类型(CharField)的数据，CharField字段必须执行max_length参数，它表示设置字符长度，如果超出这个长度，就会失败。
    p_name = models.CharField(max_length=20)
    # IntegerField()表示这个字段的值需要是整数
    p_age = models.IntegerField()


