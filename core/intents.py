def intents():
    intents = {"intents": [
    {"tag": "saludo",
     "patterns": ["Hola","yo soy el","yo soy la", "soy quien se encarga de","yo me encargo de", "holii", "Buenos dias", "Buenas tardes", "Buenas noches", "wenas","mi cargo es"],
     "responses": ["¿Que hará el sistema? ¿Qué módulos le gustaría que tuviera el sistema?"],
     "context_set": ""
    },
        {"tag": "nombre",
     "patterns": ["ni idea"],
     "responses": ["¿Quién usará el sistema? ¿Habrá tipos de usuario?", "¿Se crearán perfiles para clientes o solo para administradores?"],
     "context_set": ""
    },
            {"tag": "cargo",
     "patterns": ["lo usaran mis clientes y el administrador","serian clientes y admins","habra dos tipos de usuarios","habra 2 tipos de usuarios","habra 2 tipos de usuarios, clientes y administradores","solo lo usaremos nosotros","Para ambos", "para clientes", "solo para mi", "solo para cliente", "para admin", "para administrador", "para administradores", "solo para admins"],
     "responses": ["¿Se requiere algún tipo de seguimiento como contador de visitas, de perfiles creados o de ventas?"],
     "context_set": ""
    },
            {"tag": "web",
     "patterns": ["Si, un contador de visitas", "contador de visitas","contador de perfiles creados","contador de vantas","contador","cotador","contador de visitas y ventas", "me gustaria un contador de visitas", "un contador de visitas seria bueno", "seria un contador de visitas y de ventas", "me gustaria un contador de ventas y de visitas", "un contador de ventas", "me gustaria un contador de ventas"],
     "responses": ["¿Se requiere pasarela de pagos con tarjeta de crédito, PSE o tarjeta débito?"],
     "context_set": ""
    },
            {"tag":"SO", 
     "patterns": ["si, los 3","los 3","todos","se requieren todos","pasarela de pagos","pagos","pagar","3","Si, si se requiere", "si, pero solo para terjetas de credito", "si, pero solo para terjetas débito","si, pero solo para pse","si, pero solo para PSE","pse", "tarjeta","targeta","tajeta","tarjeta de credito", "tarjeta debito","PSE"],
     "responses": ["¿Los datos de la página web serán estáticos o requieren de interacción con alguna base de datos?", "El contenido de la página web. ¿Requiere del uso de una base de datos?"],
     "context_set": ""
    },
            {"tag":"Navegador",
     "patterns": ["Seran estaticos","los datos vendran de una base de datos","me gustaria interaccion con la base de datos","El contenido sera dinamico","contenido","base de datos","bd","estatico","la idea es que lo haga yo mismo","serian fijos","quisiera que fueran fijos", "quisera tener una base de datos", "quisiera que se manejara con base de datos"],
     "responses": ["¿Los datos de la pagina web seran estaticos o requieren de interacción con la base de datos?"],
     "context_set": ""
    },        {"tag": "bd",
     "patterns": ["Seran estaticos","la idea es que lo haga yo mismo","serian fijos","quisiera que fueran fijos", "quisera tener una base de datos", "quisiera que se manejara con base de datos"],
     "responses": ["¿Se requiere alguna interacción con el cliente, tal como un chat, campañas de sms, envío de correos electrónicos o foros de discusión"],
     "context_set": ""
    },
      {"tag": "perfil", 
     "patterns": ["Si, foros de discusión","campañas de sms","sms","los 4","se requieren los 4","4", "me gustaria un foro de discusion", "foros de discusion", "foros de discucion y chats","quisiera un chat", "chat","chats","foros de discusion", "Chat", "quiero un chat y un foro de discusion", "quiero un manejo de emails","quiero emails","email","e-mail","mails","E-mail", "e mail", "quiero E-mails, foros de discusión y chat", "discucion", "Discucion"],
     "responses": ["Muchas gracias por la información, ¿le gustaría agendar una cita con el analista de software para definir el alcance del proyecto y discutir el detalle de los requerimientos?”],
     "context_set": ""
    },
        {"tag": "seguimiento",
     "patterns": ["si, me gustaria","si me gustaria agendar un cita","si, quisiera agendar una cita","me encantaria"],
     "responses": ["¿Qué día le parece adecuado?", "Por favor, agende la fecha y hora de preferencia para la reunión"],
     "context_set": ""
    },
            {"tag": "contador",
     "patterns": ["proxima semana","la proxima semana","semana","Semana","me gustaria la proxima semana", "lunes","martes","miercoles","jueves","viernes","sabado","domingo","el proximo lunes","el proximo martes","el proximo miercoles","el proximo jueves","el proximo viernes","hora","a las","de la mañana","de la tarde","mañana","pasado mañana","pasado mañana","am","pm","2020","10/2020","11/2020","medio dia","y media","y quince minutos","y quince","minutos", "para el","octubre","noviembre","diciembre","de octubre","de noviembre","fin de semana"],
     "responses": ["Muchas gracias, nos comunicaremos con usted en la fecha acordada"],
     "context_set": ""
    },
            {"tag": "discusion",
     "patterns": ["no","por el momento no","aun no","no estoy interesado", "por el momento no, gracias"],
     "responses": ["De acuerdo, por favor comuniquese con nosotros al correo taker@taker.com, cuando cambie de opinion"],
     "context_set": ""
    }
]
}

    return intents