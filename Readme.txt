###############################################
###############################################
########   Proyecto Final Blog-Coder ##########
###############################################
###############################################

     Autor: Luciano Pardo - Comisión: 34640 

===============================================

* Descripción: 


Se trata de una Web tipo blog realizada utilizando el framework de Django como proyecto final del curso de Python en CoderHouse.

===============================================


* Instrucciones de uso:


  1. Clonar el proyecto

  2. Crear las migraciones ejecutando <python manage.py makemigrations> y luego <python manage.py migrate>

  3. Iniciar la aplicación con <python manage.py runserver>

Una vez inicializada la aplicación, el usuario tendrá disponible la URL de Inicio y podrá navegar dentro de las distintas páginas disponibles 

===============================================

* Módulos y Especificaciones: 


Este Portal cuenta con cuatro Módulos: Posts, About Me, Mensajes y Profile. 

El modulo Posts se puede acceder sin la necesidad de estar logueado. Una vez seleccionada esta opción nos llevara a la página que muestra el listado de los Posts cargados en el Portal. 

Podremos "Leer" o "Borrar" cada uno de los Post así como también crear un nuevo Post en caso de que se desee. 

Esta página también cuenta con la opción de "Volver a Inicio" la cual nos regresara al Home Page. 


El módulo de Mensajes cuenta con una bandeja de entrada en la que se podrá observar todos los mensajes y tiene la opción e Escribir un nuevo mensaje. 

Si seleccionamos un mensaje en particular la aplicación lo marcara automáticamente como leído y nos derivara a una nueva página que nos ofrecerá la opción de responderlo. 

En cambio cuando ingresamos a los mensajes enviados solo tendremos la opcion de leerlos. 

Cabe destacar que este módulo puede accederse únicamente estando Logueado en el sistema. 



El módulo Perfil cuenta con cuatro opciones: registración, buscar, listar y editar Profile. 

Seleccionando la opción de registración podremos crear un nuevo usuario ingresando: Username, Email y Contraseña. 

Si seleccionamos la opción Buscar se nos solicitara un nombre de usuario que al ser ingresado nos devolverá su username y Email. 

La opción Listar nos mostrara todos los usuarios creados en la base y nos ofrecerá la opción de Borrarlos en caso deseado. 

Y por último si seleccionamos la opción Editar Profile nos permitirá agregar una Bio del usuario, seleccionar un Avatar e incluir un sitio Web. 


En cuanto a la navegación en general cabe mencionar que una vez logueado el nombre del usuario aparecerá en la barra superior con su correspondiente avatar (en caso de que se haya incluido en el Profile). 

también se incluyó un Icono con la opción de LOGOUT la cual una vez seleccionada cerrara la sesión del usuario logueado. 

===============================================