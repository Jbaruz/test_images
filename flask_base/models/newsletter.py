import os

from flask_base.config.mysqlconnection import connectToMySQL
from flask_base.models.modelo_base import ModeloBase
from flask import flash

class News(ModeloBase):
    
    modelo = 'news'
    campos = ['title','resume','category','content']


    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.resume = data['resume']
        self.category = data['category']
        self.content = data['content']
        self.image = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_width_picture(cls):
        query = f"SELECT * FROM {cls.modelo} JOIN pictures ON {cls.modelo}.id = new_id;"
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query)
        print("AQUI QUIERO VER 22222-->",results)
        all_data = []
        for data in results:
            # data['name'] = ''
            all_data.append(cls(data))
            print("VER DATA--->", data)
            print("VER ALL_DATA--->", all_data)
        return all_data
    
    @staticmethod
    def validar_largo(data, campo, largo):
        is_valid = True
        if len(data[campo]) <= largo:
            flash(f'El largo del {campo} no puede ser menor o igual {largo}', 'error')
            is_valid = False
        return is_valid

    @classmethod
    def validar(cls, data):

        is_valid = True

        is_valid = cls.validar_largo(data, 'title', 3)
        if not is_valid:
            is_valid = cls.validar_largo(data, 'resume', 3)
            is_valid = False
        if not is_valid:
            is_valid = cls.validar_largo(data, 'category', 3)
            is_valid = False
        if not is_valid:
            is_valid = cls.validar_largo(data, 'content', 9)
            is_valid = False
        return is_valid
