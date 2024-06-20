#CREAR BASE DE DATOS
DROP DATABASE IF EXISTS Tarea;
CREATE DATABASE Tarea;
#USAR TABLA
USE Tarea
#CREAR TABLE TIPO USUARIO
CREATE TABLE TipoUsuario(
	IdTipoUsuario VARCHAR(50) PRIMARY KEY NOT NULL
)ENGINE=INNODB;
#CREAR TABLA USUARIO
CREATE TABLE Usuario(
	IdUsuario INT PRIMARY KEY AUTO_INCREMENT,
	IdTipoUsuarioU VARCHAR(50) NOT NULL,
	NOMBRE VARCHAR(100) NOT NULL,
	EMAIL VARCHAR(100) NOT NULL,
	CONTRASENA VARCHAR(10) NOT NULL,
	FOREIGN KEY (IdTipoUsuarioU) REFERENCES TipoUsuario(IdTipoUsuario)
)ENGINE=INNODB;
#CREAR TIPONOTA
CREATE TABLE TipoNota(
	IdTipoNota VARCHAR(50) PRIMARY KEY NOT NULL
)ENGINE=INNODB;
#CREAR TABLA NOTAS
CREATE TABLE Notas(
	IdNotas INT PRIMARY KEY AUTO_INCREMENT,
	IdTipoNotaN VARCHAR(50) NOT NULL,
	Titulo LONGTEXT NOT NULL,
	Contenido LONGTEXT NOT NULL,
	FOREIGN KEY (IdTipoNotaN) REFERENCES TipoNota(IdTipoNota)
)ENGINE=INNODB;
#CREAR TABLA NOTAU
CREATE TABLE NotaU(
	IdNota INT PRIMARY KEY AUTO_INCREMENT,
	IdNotaU INT NOT NULL,
	IdUsuarioU INT NOT NULL,
	FOREIGN KEY (IdNotaU) REFERENCES Notas(IdNotas),
	FOREIGN KEY (IdUsuarioU) REFERENCES Usuario(IdUsuario)
)ENGINE=INNODB;

#Insertar tipos de Usuarios
INSERT INTO TIPOUSUARIO (IdTipoUsuario) VALUES ("Docente"),("Estudiante");

#Insertar Usuarios
INSERT INTO Usuario(IdTipoUsuarioU, NOMBRE, EMAIL, CONTRASENA) VALUES ("Docente", "Jose", "jose@123", "123"),
		   ("Estudiante", "Jose", "jose@1234", "1234"), ("Estudiante", "Jose", "jose@12345", "12345");

#Insertar Tipo de notas
INSERT INTO TipoNota(IdTipoNota) VALUES ("Tarea"), ("Recordatorio");

#Insertar Nota
INSERT INTO Notas(IdTipoNotaN, Titulo, Contenido) VALUES ("Tarea", "Tarea 1", "Hacer la tarea 1"), ("Recordatorio", "Tarea 2", "Hacer la tarea 2");

#Insertar nota con usuario
INSERT INTO NotaU(IdNotaU, IdUsuarioU) VALUES (1, 1), (2,1);





	