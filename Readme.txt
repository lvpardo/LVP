###############################################
###############################################
########   Proyecto Final Blog-coder ##########
###############################################
###############################################

     Autor: Luciano Pardo - Comision: 34640 

===============================================

* Instrucciones de uso:

Se trata de una web tipo blog realizada utilizando el framework de Django como proyecto final del curso de Python en CoderHouse.

  1. Clonar el proyecto

  2. Crear las migraciones ejecutando <python manage.py makemigrations> y luego <python manage.py migrate>

  3. Iniciar la aplicación con <python manage.py runserver>

Una vez inicializada la aplicación, el usuario tendra disponible la URL de Inicio y podra navegar dentro de las distintas páginas disponibles 

===============================================

* Modulos y Especificaciones: 


Este Portal cuenta con cuatro Modulos: Posts, About Me, Mensajes y Profile. 

El modulo Posts se puede acceder sin la necesidad de estar logueado. Una vez seleccionada esta opcion nos llevara a la pagina que muestra el listado de los Posts cargados en el Portal. 

Podremos "Leer" o "Borrar" cada uno de los Post asi como tambien crear un nuevo Post en caso de que se desee. 

Esta Pâgina tambien cuenta con la opcion de "Volver a Inicio" la cual nos regresara al Homepage. 



El modulo de Mensajes cuenta con una bandeja de entrada en la que se podran observar todos los mensajes y tiene la opcion e Escribir un nuevo mensaje. 

Si seleccionamos un mensaje en particular la aplicacion lo marcara automaticamente como leido y nos derivara a una nueva pagina que nos ofrecera la opcion de responderlo. 

En cambio cuando ingresamos a los mensajes enviados solo tendremos la opcion de leerlos. 

Cabe destacar que este modulo puede accederse unicamente estando Logueado en el sistema. 



El modulo Perfil cuenta con cuatro opciones: Registracion, Buscar, Listar y editar Profile. 

Seleccionando la Opcion de Registracion podremos crear un nuevo usuario ingresando: Username, Email y Contraseña. 

Si seleccionamos la opcion Buscar se nos solicitara un nombre de usuario que al ser ingresado nos devolvera su username y Email. 

La opcion Listar nos mostrara todos los usuarios creados en la base y nos ofresera la opcion de Borrarlos en caso deseado. 

Y finalmente la opcion Editar Profile nos permitira agregar una Bio del usuario, seleccionar un Avatar e incluir un sitio Web. 



En cuanto a la navegacion en general cabe mencionar que una vez logueado el nombre del usuario aparecera en la barra superior con su correspondiente avatar (en casa de que se haya incluido en el Profile). 

Tambien se incluyo un Icpno con la opcion de LOGOUT la cual una vez seleccionada cerrara la sesion del usuario logueado. 

===============================================

