from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user
from flask_admin.form.upload import ImageUploadField
import os
from models import db, User, Product


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))

admin = Admin(template_mode="bootstrap3", index_view=MyAdminIndexView())

# Views

class ProductView(ModelView):
    form_extra_fields = {
        'image': ImageUploadField('image', base_path='uploads')
    }

    def on_model_delete(self, model):
        if model.image:
            image_path = os.path.join('uploads', model.image)
            if os.path.exists(image_path):
                os.remove(image_path)

admin.add_view(ModelView(User, db.session))
admin.add_view(ProductView(Product, db.session))