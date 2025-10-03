
-- Script de Base de Datos para el Proyecto Flask (Almacenes Sony)
-- Base de datos: almacenes_sony

DROP DATABASE IF EXISTS almacenes_sony;
CREATE DATABASE almacenes_sony;
USE almacenes_sony;

-- Tabla usuarios (para login)
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

-- Tabla ventas (relación con usuarios y productos)
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
);

-- Insertar datos de prueba
INSERT INTO usuarios (username, password, nombre) VALUES
('admin', 'admin123', 'Administrador'),
('user1', 'user123', 'Juan Pérez');

INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Televisor Sony 55"', 'Televisor LED 55 pulgadas 4K', 750.00, 10),
('PlayStation 5', 'Consola de videojuegos Sony PS5', 500.00, 5),
('Audífonos Sony WH-1000XM4', 'Audífonos inalámbricos con cancelación de ruido', 300.00, 15);
