### flask 核心简单可扩展


1. 安装虚拟环境enve
	sudo yum install python-virtualenv
	python2 -m virtualenv venv
	. venv/bin/activate

	\Python27\Scripts\virtualenv.exe venv
	venv\Scripts\activate

	pip install Flask


2. 运行
	set FLASK_APP=hello.py
	flask run


3.	路由,请求,响应，重定向，cookie，session，文件上传，json，日志，消息闪现
	route()装饰器
	路由匹配： <converter:variable_name; /path/<path:subpath>; /path/<int:age>; /path/<float:weight>；string/uuid;
	url_for 本地环境 with app.test_request_context()
	render_templates
	request.methods=[]



