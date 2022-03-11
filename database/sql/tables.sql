CREATE TABLE IF NOT EXISTS table_data( -- crea la table_data tasks si no existe 
-- Esta tabla es para manejar las tareas del usuario
    id INTEGER PRIMARY KEY, --llave primaria 
    temperatura TEXT NO NULL, --texto
    ph TEXT NO NULL, -- float
    created_date TEXT NO NULL, -- la fecha de creacion
    created_time TEXT NO NULL -- el tiempo de los datos
)