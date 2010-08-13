def register_modules(app, mod_list):
    for mod in mod_list:
        app.register_module(mod)
