intents = {"intents": [
    {"tag": "saludo",
     "patterns": ["Hola", "holii", "Buenos dias", "Buenas tardes", "Buenas noches", "wenas"],
     "responses": ["Hola, gracias por reunirse conmigo. ¿me podria indicar con quien estoy hablando?","Buenas, gracias por esta reunion. ¿me podria indicar con quien estoy hablando?"],
     "context_set": ""
    },
        {"tag": "nombre",
     "patterns": ["yo soy","mi nombre es","me llamo"],
     "responses": ["¿que cargo desempeña?","¿cual es el cargo que desempeña?"],
     "context_set": ""
    },
            {"tag": "cargo",
     "patterns": ["yo soy el","yo soy la", "yo trabajo de","mi cargo es", "soy el", "soy la","soy el encargado de", "yo soy la encargada de","soy el dueño", "soy la dueña"],
     "responses": ["Para empezar, ¿Quisiera una aplicación web o aplicación movil?"],
     "context_set": ""
    },
            {"tag": "web",
     "patterns": ["quiero una pagina web", "quiero una aplicacion web", "pagina web", "aplicación web", "quiero una pagina de internet","una pagina de internet"],
     "responses": ["¿Sobre que Sistema Operativo quisiera que se manejara esta aplicación web?"],
     "context_set": ""
    },
            {"tag":"SO", 
     "patterns": ["Windows", "Windows y Linux", "solo Windows estaria bien", "en todos", "En todos los sistemas operativos"],
     "responses": ["¿En que navegador quisiera que se use?", "En que navegador se deberia usar la pagina web?","¿sobre que navegador se usara?", "¿tiene alguna preferencia sobre el navegador?"],
     "context_set": ""
    },
            {"tag":"Navegador",
     "patterns": ["google", "google chrome", "crome", "google crome", "opera", "google y opera","en todos los navegadores","en internet explorer"],
     "responses": ["¿Los datos de la pagina web seran estaticos o requieren de interacción con la base de datos?"],
     "context_set": ""
    },        {"tag": "bd",
     "patterns": ["Seran estaticos","la idea es que lo haga yo mismo","serian fijos","quisiera que fueran fijos", "quisera tener una base de datos", "quisiera que se manejara con base de datos"],
     "responses": ["¿Se crearan perfiles para clientes o solo para administradores?"],
     "context_set": ""
    },
      {"tag": "perfil", 
     "patterns": ["Seran estaticos","la idea es que lo haga yo mismo","serian fijos","quisiera que fueran fijos", "quisera tener una base de datos", "quisiera que se manejara con base de datos"],
     "responses": ["¿Se crearan perfiles para clientes o solo para administradores?"],
     "context_set": ""
    },
        {"tag": "seguimiento",
     "patterns": ["Para ambos", "para clientes", "solo para mi", "solo para cliente", "para admin", "para administrador", "para administradores", "solo para admins"],
     "responses": ["¿Se requiere algun tipo de seguimiento como contador de visitas o de perfiles creados o de ventas?"],
     "context_set": ""
    },
            {"tag": "contador",
     "patterns": ["Si, un contador de visitas", "me gustaria un contador de visitas", "un contador de visitas seria bueno", "seria un contador de visitas y de ventas", "me gustaria un contador de ventas y de visitas", "un contador de ventas", "me gustaria un contador de ventas"],
     "responses": ["¿Se requiere alguna interacción con el cliente, tal como un chat, E-mail o foros de discusión"],
     "context_set": ""
    },
            {"tag": "discusion",
     "patterns": ["Si, foros de discusión", "me gustaria un foro de discusion", "foros de discusion", "foros de discucion y chats","quisiera un chat", "chat","chats","foros de discusion", "Chat", "quiero un chat y un foro de discusion", "quiero un manejo de emails","quiero emails","email","e-mail","mails","E-mail", "e mail", "quiero E-mails, foros de discusión y chat", "discucion", "Discucion"],
     "responses": ["¿Se requiere pasarelo de pagos con tarjeta de crédito, pse o tarjeta débito?"],
     "context_set": ""
    },
            {"tag": "pago",
     "patterns": ["Si, si se requiere", "si, pero solo para terjetas de credito", "si, pero solo para terjetas débito","si, pero solo para pse","si, pero solo para PSE","pse", "tarjeta","targeta","tajeta","tarjeta de credito", "tarjeta debito","PSE"],
     "responses": ["Muchas gracias por la atención, me gustaria agendar una cita esta misma semana para definir el alcance del proyecto y discutir nuevos requerimientos. ¿Que dia le parece adecuado? "],
     "context_set": ""
    }
]
}

