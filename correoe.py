import smtplib
import sendmail
from smtplib import *


########################################################################################################################################
#Para poder accesar con la libreria smtplib es necesario seguir los siguientes pasos:
#En la linea de comandos poner: pip install sendmail y:
#0-Solo se pueden enviar correos con el dominio de gmail, ya que para otros dominios no encontré como se hacía, mas que con yahoo
#Afortunadamente la mayoria de negocios usan gmail, por eso de las opciones que nos da para ubicación, anuncios etc.
#1-Debes entrar a tu bandeja de entrada de tu correo
#2-En la imagen de nuestro perfil debemos dar click para que aviente el menú
#3-Damos click en administración de cuenta de Google
#4-Buscamos donde diga Seguridad
#5-En "Acceso a Google" deben aparecer las opciones de verificación de dos pasos y la de Contraseñas de aplicaciones
#6-Si no aparece Contraseñas de aplicaciones olvidalo, no se puede hacer más
#7-Al acceder te pide tu contraseña
#8-Al seleccionar el primer campo de seleccionar app, le das a (otros), y lo nombras como gustes
#9-automaticamente al dar el nombre genera un código con el cual podrás obtener el código
#Solo así se pueden enviar correos con esta libreria, intenté crear una nueva cuenta especifia para este 
#Pero no se pudo, ya que a partir de marzo de este año ya no deja hacerlo por temas de seguridad y hackeo
########################################################################################################################################
class mails:

    def __init__(self):
        self.politics_Cancel="\nPolítica de cancelación\n Al reservarte un espacio en agenda, no podemos ofrecerlo a nadie más. Es por ello que debes tomar en cuenta lo siguiente:\n Si cancelas tu cita con más de 72 horas de anticipación, no habrá ningún cargo. Podrás escoger un nuevo turno según la disponibilidad de la agenda.\n Si cancelas tu cita con menos de 24 horas de antelación, se cobrará el costo completo de tu sesión. No hay excepciones para esto. Ya que si no nos avisas a tiempo, no podremos utilizar este tiempo de tu cita con otra persona."
#
        self.politics_cita ="\nPolítica de citas\n Nos esforzamos por darte un servicio de calidad, y en ayudarte a agendar una cita a la brevedad posible.\n Es nuestro deseo ser efectivos y justos con todas las personas que atendemos y, en consideración a su tiempo, hemos adoptado las siguientes políticas: \n Pago de cita y reserva de turno:\n El turno sólo será reservado al recibir el pago, en caso contrario, seguirá estando disponible  y podrá ser asignado a otra persona sin previo aviso. \nPuntualidad:\n Te recomendamos estar listo un par de minutos antes de la hora de inicio de la sesión para que podamos empezar a tiempo. No podemos extender las citas si asistes tarde, pues otro cliente puede estar esperando. \nConfidencialidad:\n Nuestro servicio es completamente confidencial. No hablaremos con nadie sobre ningún aspecto de tu sesión sin tu consentimiento.\nComentarios:\n Si no estás satisfecho con algún aspecto de la atención que te hemos brindado, háznoslos saber a la brevedad. Trabajaremos contigo para resolver cualquier problema.\n\n"
        self.envia_correoconfirm()
        

#sección de variables string para pasar los valores más adelante=======================================================================
gmailUser= "krazilegh2000@gmail.com"
#Aqui debajo está el codigo que me dió google
gmailPasswd="iqogwjlcoolbgrmi"
        # Ingresa tu correo para que pueda enviarlo desde ahí=======================================================================
#remitente = "edson2109@outlook.com"


#==============================================================================================================================================
#                                            ------------Inicio del código funcional------
def envia_correoconfirm():
        print("CONECTANDO A GMAIL")
try:
    #Hace una conexion al servidor
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        #EHLO: para abrir una sesión, en el caso de que el servidor soporte extensiones definidas en el RFC 1651. MAIL FROM: para indicar quien envía el mensaje.
        print("SE HA CONECTADO")
        print("HACIENDO LA CONEXIÓN SEGURA")
        
        try:
            server.starttls()
            #STARTTLS es una manera de transformar una conexión insegura ya existente a segura con SSL/TLS, sin utilizar un puerto diferente para la conexión cifrada.
            print("CONEXIÓN SEGURA")
        except :
            print("CUIDADO: NO ES SEGURO ENVIAR ESTE CORREO")
        #gmailUser = myGmail
        #gmailPasswd = myGMPasswd
        
        
        print("CHECANDO USUARIO Y CONTRASEÑA")
        try:
            server.login(gmailUser, 'iqogwjlcoolbgrmi')
            #se encarga de la autenticación del usuario (comprobando que el nombre de usuario y contraseña sean correctos), y establece un entorno inicial para el usuario activando permisos para la línea serie e iniciando el intérprete de comandos.
            print("USUARIO Y CONTRASEÑA CORRECTOS")
        except :
            print("TU USUARIO, CONTRASEÑA O AMBOS SON INCORRECTOS")            
            quit
            
        recipient = "itamarsarahih@gmail.com"
        #Remitente del correo, a quien será enviado, aqui si se puede poner cualquier correo con cualquier dominio, ya que 
        #el que se encarga de verificar que se enviado es google y no la libreria misma
        #MA = "Gracias por reservar una cita con nosotros.\n Te esperamos en Namaste, en el dia y hora acordados: \n"
        #MM="--------------------Modificación--------"
        #message="Recuerda ser puntual, para no influir en los horarios de otros clientes, gracias."+str(recipient)
        fecha= "-12-"
        nombredado= "pochoclo"
        nombre="Hola: "+ nombredado
        message ="\n mmmm"+ str(nombre) +"\n"+ str(fecha) 
        #plantilla para el correo     
        print("ENVIANDO CORREO")
        try:
            #Formato para enviar correo
            server.sendmail("krazilegh2000@gmail.com", recipient,str(message))
            print("MENSAJE ENVIADO DESDE: " + gmailUser)
            quit
        except:
                print("UN ERROR HA OCURRIDO AL ENVIAR EL CORREO")
                quit
except:
        print("NO SE PUEDE CONECTAR A GMAIL")
        quit             
        
