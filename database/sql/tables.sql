CREATE TABLE IF NOT EXISTS table_data( -- crea la table_data tasks si no existe 
-- Esta tabla es para manejar las tareas del usuario
    id INTEGER PRIMARY KEY, --llave primaria 
    temperatura FLOAT(2,1), --float
    ph FLOAT(2,1), -- float
    created_date TEXT NO NULL -- la fecha de creacion
)