# Log of building the studentLife website

[TOC]

## Get to know AWS Server

[新手教程－如何在 Amazon AWS 上搭建和部署网站](http://www.awshao.com/新手教程－如何在-amazon-aws-上搭建和部署网站/)

[Tutorial: Install a LAMP web server on Amazon Linux 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html)

[Tutorial: Configure SSL/TLS on Amazon Linux 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2.html)

[Tutorial: Host a WordPress blog on Amazon Linux 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html#create_user_and_database)

## Get to know web development

[Getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Getting_started)
[What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
[Web forms — Working with user data](https://developer.mozilla.org/en-US/docs/Learn/Forms)
[Getting started with React](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_getting_started)
[Getting started with Ember](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Ember_getting_started)
[Getting started with Vue](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started#.vue_files_single_file_components)
[Getting started with Svelte](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Svelte_getting_started)
[Getting started with Angular](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Angular_getting_started)
[Introduction to the server side](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction)
[Django introduction](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
[Express/Node introduction](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction)
[Node.js是用来做什么的？](https://www.zhihu.com/question/33578075)
[Introduction to Node .js](http://nodejs.cn/learn)

## Learn to build local web using Django

[Django Tutorial: The Local Library website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)

## Put login web on the AWS server

### Delete and recreate the instance of server

之前使用的aws linux 2很难用，换成ubuntu，采用20（18的仍有python2），22刚发布暂不用

### Set static IP

13.215.90.183

### Rent Domain

studentlife.club

### Git clone a login repo

[Django-registration-and-login-system](https://github.com/earthcomfy/Django-registration-and-login-system)

### Install apache

[Install and Configure Apache](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview)

### Use python virtual env

[Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
[How to install a package inside virtualenv?](https://stackoverflow.com/questions/21240653/how-to-install-a-package-inside-virtualenv)
[Could not install packages due to an EnvironmentError: [Errno 13]](https://stackoverflow.com/questions/52949531/could-not-install-packages-due-to-an-environmenterror-errno-13)

### Install mod-wsgi

可以用[pip安装](https://pypi.org/project/mod-wsgi/)或从[源码安装](https://modwsgi.readthedocs.io/en/master/user-guides/quick-installation-guide.html)，这里选择用[pip安装](https://pypi.org/project/mod-wsgi/)，并进行将mod-wsgi的位置写入apache2配置文件的配置

另可参考：[Django 上的静态 STATIC_URL 和 STATIC_ROOT 之间的区别](https://stackoverflow.com/questions/8687927/difference-between-static-static-url-and-static-root-on-django)

### Configure Apache to manage Django

[How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/modwsgi/)

### Configure SSL

[certbot instructions](https://certbot.eff.org/instructions?ws=apache&os=ubuntufocal)

[Name duplicates previous WSGI daemon definition](https://stackoverflow.com/questions/39317200/name-duplicates-previous-wsgi-daemon-definition)

certbot复制了原本/etc/apache2/sites-available/studentLifeWeb.conf的内容，并创建了studentLifeWeb-le-ssl.conf文件，同时使apache2使能该文件，因此去掉之前加了注释的WSGI*的语句就可以消除转发mod-wsgi失败的问题（表现为访问网站回到了默认页面）

## StudentLife web design

1. 首先，这是一个课程评论网站，主要用户是高校学生
2. 给用户添加属性
   1. 所在学校
   2. 所在专业
   3. 所选课程
3. 课程评论作为一个单独的Django app
4. 课程评论的数据库
   1. 学校ID（primary key），学校名称，学校简介
   2. 课程ID（primary key），课程名称，课程简介，课程所在学校，课程所在院系，课程教授，课程评分均分
   3. 教授ID（primary key），教授名称，教授简介，教授所在学校，教授所在院系，教授的课程，教授的课程评分均分
   4. 评论ID（primary key），发表评论的用户，评论的课程，评论内容，评论时间，评论打分，评论用户的该课程得分，学习到的内容打分
5. 课程评论的视图
   1. 用户登录后，点击按钮跳转到学校搜索页面，并显示热门搜索学校
   2. 搜索结果页面，显示搜索到的学校
   3. 点击学校进入课程搜索页面，并显示热门搜课程
   4. 搜索结果页面，显示搜索到的课程
   5. 点击课程可以进入课程详情页面，显示所有的课程信息和对该课程的评论，并且可以让用户将课程加入自己的课程表，也可以发表评论
   6. 发表评论页面，显示一条评论所需要的所有信息，利用表单提交
6. 用户的个人中心显示其个人信息，其所选课程
7. 加入添加好友功能，使不认识的人可以相互认识讨论
8. 加入学习资源功能，在课程页面上加入高质量的学习资源，书、课程推荐等

## Coding

### Instructions

跟随教程，按步骤编写：[Django介绍](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)

### Pass parameters from URL to View

[How To Pass Parameters To View Via Url In Django](https://www.dev2qa.com/how-to-pass-parameters-to-view-via-url-in-django/)

[URL-parameters and logic in Django class-based views (TemplateView)](https://stackoverflow.com/questions/15754122/url-parameters-and-logic-in-django-class-based-views-templateview)

### Generic View

[Generic display views¶](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/)

[Django: detail view must be called with pk or slug](https://www.valentinog.com/blog/detail/)

### Django reverse

[django.urls utility functions](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/)

### Filter in get_queryset()

[Filtering](https://www.django-rest-framework.org/api-guide/filtering/#filtering)

### access more context data in template(html)
[No need to use get_context_data, use {{ view.some_method }}](https://reinout.vanrees.org/weblog/2014/05/19/context.html#:~:text=Behind%20the%20scenes%2C%20it%20is%20the%20ContextMixin%20that,doesn%E2%80%99t%20allow%20you%20to%20call%20methods%20like%20that.)

### manyToManyField Obejcts
[How to Retrieve All Objects of a ManyToManyField in Django](http://www.learningaboutelectronics.com/Articles/How-to-retrieve-all-objects-of-a-ManyToManyField-in-Django.php#:~:text=A%20ManyToManyField%20in%20Django%20is%20a%20field%20that,ManyToManyField%2C%20we%20can%20use%20the%20add%20%28%29%20function.)

### HTML Table
[<table>: The Table element](https://developer.mozilla.org/en-US/docs/web/html/element/table#deprecated_attributes)
