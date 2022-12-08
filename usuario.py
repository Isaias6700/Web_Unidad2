from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from ..extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idusuario = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    correo = Column(String(200), unique=True, nullable=False)
    clave = Column(String(200))
    activo = Column(Integer, default=1)

class Estudiantes(db.Model):
    __tablename__ = 'estudiantes'
    idEstudiante= Column(Integer,primary_key=True)
    aluControl = Column(Char(10), unique=True, nullable=False)
    aluApP = Column(String(100), unique=True, nullable=False)
    aluApM = Column(Char(100), unique=True, nullable=False)
    aluNom = Column(String(100), unique=True, nullable=False)
    aluSex= Column(Integer, unique=True, nullable=False)
    aluNac= Column(Date, unique=True, nullable=False)
    aluRFC= Column(Char(13), unique=True, nullable=False)
    aluESC= Column(Integer, unique=True, nullable=False)

class UsoEstudiantes(db.Model):
    __tablename__ = 'usoEstudiantes'
    idUsoEstudiante = Column(Integer, primary_key=True)
    FechaIngreso= Column(Date, unique=True, nullable=False)
    FechaTermino= Column(Date, unique=True, nullable=True)
    activo = Column(Integer, default=1)

    idEstudiante = Column(Integer, ForeignKey('estudiantes.idEstudiantes'))
    idUsuarios = Column(Integer, ForeignKey('estudiantes.idEstudiantes'))
    estudiantes = db.relationship ("Estudiantes", backref='usoEstudiantes', order_by=idUsoEstudiante)
    usuarios = db.relationship ("Usuarios", backref='usoEstudiantes', order_by=idUsoEstudiante)

class PadresFamilia(db.Model):
    __tablename__ = 'padresFamilia'
    idPadresFamilia =Column(Integer, primary_key=True)
    Apellidos =  Column(String(200), unique=False, nullable=False)
    Nombre = Column(String(100), unique=False, nullable=False)
    Sexo = Column(Integer, unique=False, nullable=False)
    EstadoTrabajo = Column(Integer, unique=False, nullable=False)
    TelTrabajo = Column(Char(12), unique=True, nullable=False)
    EstadoVido = Column(Integer, nullable=True, nuallable=False)

class PadresEstudiantes(db.Model):
    __tablename__ = 'padresEstudiantes'
    idPadreEstudiantes = Column(Integer, primary_key=True)

    idPadresFamilia = Column(Integer, ForeignKey('padresFamilia.idPadresFamilia'))
    idEstudiante = Column(Integer, ForeignKey('estudiantes.idEstudiante'))
    padresFamilia = db.relationship("PadresFamilia", backref='padresEstudiantes', order_by=idPadreEstudiantes)
    estudiantes = db.relationship ("Estudiantes", backref='padresEstudiantes', order_by=idPadreEstudiantes)

class UsuPadres(db.Model):
    __tablename__ = 'usuPadres'
    idUsuPadres = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date, unique=False, nullable=False)
    FechaTermino = Column(Date, unique=False, nullable=False)
    activo = Column(Integer, default=1)

    idUsuarios = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPadresFamilia = Column(Integer, ForeignKey('padresFamilia.idPadresFamilia'))
    padresFamilia = db.relationship("PadresFamilia", backref='usuPadres', order_by=idUsuPadres)
    usuarios = db.relationship("Usuarios", backref='usuPadres', order_by=idUsuPadres)

class Personal(db.Model):
    __tablename__ = 'personal'
    idPersonal = Column(Integer, primary_key=True)
    nt = Column(Integer, unique=True, nullable=False)
    Apellidos = Column(String(100), nullable=False)
    Nombre = Column(String(100), nullable=False)
    rfc = Column(Char(13), unique=True, nullable=False)
    Direccion = Column(String(200), nullable=False)
    CorreoPersonal = Column(String(200), unique=True, nullable=False)
    CorreoInstitucional = Column(String(200), unique=True, nullable=False)
    TelCelular = Column(Char(12), unique=True, nullable=False)
    TelCasa = Column(Char(12), unique=True, nullable=True)
    Plaza = Column(Char(12), unique=False, nullable=False)
    Tipo = Column(Char, unique=False, nullable=False)

class UsuarioPersonal(db.Model):
    __tablename__ = 'usurioPersonal'
    idUsuarioPersonal = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date, unique= False, nullable=False)
    FechaTermino = Column(Date, unique=False, nullable=False)
    activo = Column(Integer, default=1)

    idPersonal = Column(Integer, ForeignKey('personal.idPersonal'))
    idUsuarios = Column(Integer, ForeignKey('usuarios.idUsuario'))
    personal = db.relationship("Personal", bnackref='usurioPersonal', order_by=idUsuarioPersonal)
    usuarios = db.relationship("Usuarios", backref='usurioPersonal', order_by=idUsuarioPersonal)


   

    def __str__(self):
        return self.idusuario+"."+self.nombre+"."+self.correo

    def __repr__(self):
        return '<Usuarios %r>' % self.nombre