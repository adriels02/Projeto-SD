class CompraProdutoRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'carrinho':
            return 'default'
        if model._meta.app_label == 'produtos':
            return 'external_db'
        if model._meta.app_label == 'gestao_usuarios':
            return 'email_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'carrinho':
            return 'default'
        if model._meta.app_label == 'produtos':
            return 'external_db'
        if model._meta.app_label == 'gestao_usuarios':
            return 'email_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'carrinho':
            return db == 'default'
        if app_label == 'produtos':
            return db == 'external_db'
        if app_label == 'gestao_usuarios':
            return db == 'email_db'
        return None
    
        
