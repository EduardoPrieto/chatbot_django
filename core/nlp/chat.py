# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np

import tensorflow as tf
import random
import tflearn

nltk.download('punkt')

intentos = {"intents": [
    {"tag": "saludo",
     "patterns": ["Hola","yo soy el","yo soy la", "soy quien se encarga de","yo me encargo de", "holii", "Buenos dias", "Buenas tardes", "Buenas noches", "wenas","mi cargo es"],
     "responses": ["¿Que hará el sistema? ¿Qué módulos le gustaría que tuviera el sistema?"],
     "context_set": ""
    },
        {"tag": "nombre",
     "patterns": ["Mostrar catálogo de ventas","mostrar","catalogo","Comprar y vender","productos","mostar, comprar y vender productos","Ofrecer los productos","ofrecer ropa","Gestionar el inventario","mostrar inventario","manejar inventario","Hacer un portafolio web de los servicios","servicios","Mostrar los servicios que tiene la empresa","Tener presencia en internet para que los clientes conozcan los datos de contacto","contacto","internet"],
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
       {"tag": "bd",
     "patterns": ["Seran estaticos","la idea es que lo haga yo mismo","serian fijos","quisiera que fueran fijos", "quisera tener una base de datos", "quisiera que se manejara con base de datos","Seran estaticos","los datos vendran de una base de datos","me gustaria interaccion con la base de datos","El contenido sera dinamico","contenido","base de datos","bd","estatico","la idea es que lo haga yo mismo","serian fijos","quisiera que fueran fijos", "quisera tener una base de datos", "quisiera que se manejara con base de datos"],
     "responses": ["¿Se requiere alguna interacción con el cliente, tal como un chat, campañas de sms, envío de correos electrónicos o foros de discusión"],
     "context_set": ""
    },
      {"tag": "perfil", 
     "patterns": ["Si, foros de discusión","campañas de sms","sms","los 4","se requieren los 4","4", "me gustaria un foro de discusion", "foros de discusion", "foros de discucion y chats","quisiera un chat", "chat","chats","foros de discusion", "Chat", "quiero un chat y un foro de discusion", "quiero un manejo de emails","quiero emails","email","e-mail","mails","E-mail", "e mail", "quiero E-mails, foros de discusión y chat", "discucion", "Discucion"],
     "responses": ["Muchas gracias por la información, ¿le gustaría agendar una cita con el analista de software para definir el alcance del proyecto y discutir el detalle de los requerimientos?"],
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


# import our chat-bot intents file
import json

intents = []

intents = intentos
    
words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])

# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')

# save all of our data structures
import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )


# restore all of our data structures
import pickle
data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']



# import our chat-bot intents file

# load our saved model
model.load('./model.tflearn')


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

ERROR_THRESHOLD = 0.25
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # a random response from the intent
                    return print(random.choice(i['responses']))

            results.pop(0)

