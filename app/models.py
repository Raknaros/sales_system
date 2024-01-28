#from app import db
#from flask_login import UserMixin
#from app import login


#@login.user_loader
#def load_user(id):
#    return User.query.get(int(id))


########### USER MODEL ##############
#class User(UserMixin, db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    user_name = db.Column(db.String(20), unique=True, nullable=False)
#    password = db.Column(db.String(12), nullable=False)

#    def get_id(self): return self


######## TEAM MODEL ###########
#class Team(db.Model):
#    team_id = db.Column(db.Integer, primary_key=True)
#    team_name = db.Column(db.String(20), unique=True, nullable=False)
#    team_mascota = db.Column(db.String)
#    practices = db.relationship("Practice", backref="practice", lazy=True)


######## PRACTICE MODEL #######
#class Practice(db.Model):
#    practice_id = db.Column(db.Integer, primary_key=True)
#    practice_lenght = db.Column(db.Integer)
#    practice_date = db.Column(db.DateTime)
#    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)


######## VOUCHERS BCP ########
#class v_bcp(db.Model):
#   id=db.Column(MEDIUMINT AUTO_INCREMENT NOT NULL)
#   dato_referencial=db.Column(CHAR())
#   fecha_operacion=db.Column(date)
#   hora_operacion=db.Column(time)
#   numero_operacion=db.Column(integer)
#   importe=db.Column(numeric(9, 2))
#   adquiriente=db.Column(varchar)
#   proveedor=db.Column(varchar)
#   documento_relacionado=db.Column(varchar)
#   customer_id=db.Column(varchar)
#   observaciones=db.Column(varchar)
#   cui=db.Column(varchar,UNIQUE)



############ VENTAS ##########
#class facturas(db.Model):
#   cod_pedido=db.Column(varchar)
#   cui=db.Column(tinyint)
#   alias=db.Column(varchar)
#   guia=db.Column(varchar)
#   serie=db.Column(varchar)
#   numero=db.Column(varchar)
#   emision=db.Column(fecha)
#   ruc=db.Column(varchar)
#   nombre_razon=db.Column(varchar)
#   moneda=db.Column(varchar)
#   descripcion=db.Column(varchar)
#   unid_medida=db.Column(varchar)
#   cantidad=db.Column(varchar)
#   precio_unit=db.Column(varchar)
#   forma_pago=db.Column(varchar)
#   estado=db.Column(varchar)
#   observacion=db.Column(varchar)
#   vencimiento=db.Column(varchar)



############ FORMA DE PAGO ##############
#class forma_pago(db.Model):
#   cuota1=db.Column(varchar)
#   vencimiento2=db.Column(varchar)
#   cuota2=db.Column(varchar)
#   vencimiento3=db.Column(varchar)
#   cuota3=db.Column(varchar)