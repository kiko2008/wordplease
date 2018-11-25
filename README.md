<img src="https://github.com/kiko2008/wordplease/blob/master/general/static/wordplease.png" height="180" alt="Wordplease" />


El desarrollo es un API y una pagina web para mostrar el funcionamiento de una tweb de publicacion de blogs y sus posts 
, desarrollada con Python + Django y Django Rest Framework para el API.


## Instalación



Necesitamos tener instaladas en nuestro servidor las siguientes dependencias:



```

    cookie-parser

    cross-env

    debug

    ejs

    eslint

    express

    http-errors

    mongoose

    morgan

```

dentro del directorio raiz ejecutaremos:

```bash

npm install

```


## Desarrollo



### Inicialización de la base de datos

En el archivo **.env.example** hay un ejemplo con los datos configurables por el usuario.

Para el correcto funcionamiento de la aplicación se deberá crear un fichero **.env** con las mismas propiedades que tenemos en **.env.example** pero con los valores que necesitemos para la ejecución de la aplicación.



```bash

npm run installDB

```

este paso **inicializara** la base de datos con una serie de registros para que se pueda empezar a realizar las pruebas inmediatamente.

## Ejecución

```

dentro del directorio raiz ejecutaremos:

```bash

npm start

```

este paso arrancara la aplicación.



### Urls de prueba para el API REST


API de usuarios

Endpoint que permita a cualquier usuario registrarse indicando su nombre, apellidos, nombre de usuario, e-mail y contraseña.

```bash
POST http://localhost:8000/api/1.0/users/
{
    "first_name": "laura11",
    "last_name": "fernan",
    "username": "lauri222",
    "email": "fcofp@hotmail.com",
    "password": "kiko2008"
}
```
Endpoint que permita ver el detalle de un usuario. Sólo podrán ver el endpoint de detalle de un usuario el propio usuario o un administrador.

```bash
GET http://localhost:8000/api/1.0/users/<id_user>
```
Endpoint que permita actualizar los datos de un usuario. Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.
```bash
PUT http://localhost:8000/api/1.0/users/<id_usuario>
{
    "first_name": "laura11",
    "last_name": "fernan",
    "username": "lauri222",
    "email": "fcofp@hotmail.com",
    "password": "kiko2008"
}
```
Endpoint que permita eliminar un usuario (para darse de baja). Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.
```bash
DELETE http://localhost:8000/api/1.0/users/<id_usuario>
```


API de blogs

Un endpoint que no requiera autenticación y devuelva el listado de blogs que hay en la plataforma con la URL de cada uno. Este endpoint debe permitir buscar blogs por el nombre del usuario y ordenarlos por nombre.
```bash
GET http://localhost:8000/api/1.0/blogs/?user__username=<user_name>&ordering=title
```

API de posts

Un endpoint para poder leer los artículos de un blog de manera que, si el usuario no está autenticado, mostrará sólo los artículos publicados. Si el usuario está autenticado y es el propietario del blog o un administrador, podrá ver todos los artículos (publicados o no). En este endpoint se deberá mostrar únicamente el título del post, la imagen, el resumen y la fecha de publicación. Este endpoint debe permitir buscar posts por título o contenido y ordenarlos por título o fecha de publicación. Por defecto los posts deberán venir ordenados por fecha de publicación descendente.
```bash
GET  http://localhost:8000/api/1.0/blogs/18/get-posts?title=Primer post&ordering=title
```
Un endpoint para crear posts en el cual el usuario deberá estar autenticado. En este endpoint el post quedará publicado automáticamente en el blog del usuario autenticado.
```bash
POST http://localhost:8000/api/1.0/posts/
{
    "title" : "Primer post2",
    "introduction" : "Es mi primer post con esto vale no te parece?",
    "post_body" : "Para ser el primer post esta bastante bien no crees?",
    "url_image" : "https://picsum.photos",
    "url_video" : "https://picsum.photos",
    "pub_date" : "2018-11-25",
  	"blog" : "20",
	  "categorys":  [
      {
		    "id": "3",
		    "name": "Cultura"
	    },{
		    "id": "1",
		    "name": "Deportes"
	    }
	  ]	
}
```
Un endpoint de detalle de un post, en el cual se mostrará toda la información del POST. Si el post no es público, sólo podrá acceder al mismo el dueño del post o un administrador.
```bash
GET http://localhost:8000/api/1.0/posts/54/
```
Un endpoint de actualización de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.
```bash
PUT http://localhost:8000/api/1.0/posts/54/
{
    "title" : "Primer post2",
    "introduction" : "Es mi primer post con esto vale no te parece?",
    "post_body" : "Para ser el primer post esta bastante bien no crees?",
    "url_image" : "https://picsum.photos",
    "url_video" : "https://picsum.photos",
    "pub_date" : "2018-11-25",
	  "blog" : "20",
	  "categorys":  [
      {
		    "id": "3",
		    "name": "Cultura"
	    },{
		    "id": "1",
		    "name": "Deportes"
	    }
	  ]	
}
```
Un endpoint de borrado de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.
```bash
DELETE http://localhost:8000/api/1.0/posts/54/
```

Crear un endpoint para la subida de archivos que pueda ser usado para subir imágenes a la plataforma para luego utilizarlas como imágenes destacadas.
```bash
http://localhost:8000/api/1.0/image-featured/
```


### Web Wordplease

Wordplese es una web de ublicacion de blogs. Se haplanteado de forma que los usuarios puedan tener varios blogs asociados y estos a su vez puedan tener varios posts asociados.

Para acceder a ella una vez levantado el servidor tendremos que acceder a la url:

```bash

http://localhost:3000/home

```

Esto mostrara la home de la web, con el listado de los ultimos posts publicados. 
Tendremos la posibilidad de:

  * Acceder al listado de blogs de la aplicacion pulsando el enlace BLOGS.
  * Autenticarnos en la aplicacion y acceder a las paginas privadas pulsando el boton ENTRAR. 
  * Registrasnos en la web pulsando el boton REGISTRARSE.


Al pulsar el boton de login podremos ver la pantalla de login donde podremos autenticarnos en la aplicación. Esta accion nos llevara a la pagina de home con las opciones privadas accesibles por el usaurio:

  * Crear un nuevo blog asociado al usuario logado en la aplicacion, mediante el boton NUEVO BLOG.
  * Crear un nuevo post asociado a unos de los blogs asociados al usuario logado en la aplicacion.
  * Salir de la aplicacion, mediante el boton SALIR.


## Version



 V1.0



## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
