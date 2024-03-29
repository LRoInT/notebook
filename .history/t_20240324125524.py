from main.book import NoteBook
scope={} #设置作用域
exec(open(plugin, encoding="utf-8").read(),scope)
plugin_name=scope["name"]
plugin_func=scope[scope["name"]+"Run"]
self.plugin[plugin_name]=plugin_func 