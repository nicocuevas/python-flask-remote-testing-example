# technical-challenge

## Requirements
### Software
Node >= v10.15.1
java8 JDK
Docker >= v18.06
Docker Compose >= 1.22
sdk platform android >=v23
sdk platforms tools
sdk build tools v28.0.3
Appium >= 1.16.0

## Before to start
1) Install Java8
[https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

2) Install Nodejs
[https://nodejs.org/es/download/](https://nodejs.org/es/download/)

3) Install docker and docker-compose
[https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

4) Install Docker Android Emulator (Not required)
[https://github.com/google/android-emulator-container-scripts](https://github.com/google/android-emulator-container-scripts)

5) Add environment variable JAVA_HOME (JDK installation directory)
6) Add environment variable ANDROID_HOME (SDK installation directory)
7) Install appium:  npm install -g appium
8) Install Driver uiautomator2: npm install -g appium-uiautomator2-driver

## Install and Run
1) Clone this repo
2) Change the following settings on  docker-compose.yml before run tests:
- EMU_ANDROID (emulator device name)
- ANDROID_DEVICE (connected device name)
- APK_DIR (path directory to the apk file)
3) Open a terminal and execute on repo root:
- 1) $ docker-compose build
- 2) $ docker-compose up
4) Open a new tab or terminal and execute: $ appium (this command launch the appium server)

## Test Enpoint
1) connect an Android  device or launch an emulator
2) open an terminal and run : $ adb devices (list connected devices)
3) copy the device name and replace on following command:
$ curl -X POST  "http://localhost:8000/install/{device_name}"
4) Open the screenshots folder and check if the image was created

example:
~/Desktop/projects/technical-challenge$ curl -X POST "http://localhost:8000/install/emulator-5554"
{
    "response": "ok"
}

## Running Tests

Open a new terminal and execute on repo root:
1) $ docker-compose exec api-server /bin/bash
2) $pytest api

# Respuestas
-   ¿Cómo resolvió el problema?
Para resolver el problema usé la mayor parte del tiempo invertido en investigar. Lo primero que hice fue buscar cuáles eran los frameworks, librerias más utilizados para el testing automatizado de applicaciones, me creé unas cuentas gratuitas en plataformas de testing para ver qué utilizaban dichas plataformas para el testing automatizado. A partir de ahí llegué a la conclución que debería utilizar Appium framework para la automatización. Appium permite realizar test automation tanto para ios como android, es estable, incluye varios clientes entre ellos uno para python y hay una gran comunidad. Como tengo experiencia en python, utilizar flask para la creación de servicios me parece la mejor opción para este caso.
Luego tuve que leer acerca de emuladores android y todo lo que necesité instalar para correr las automatizaciones. De hecho, encontré un repositorio de google que facilita la creación de emuladores usando docker, que es lo que utilicé para correr los scripts.
Con la investigación previa hecha, determiné cuáles iban a ser las tecnologías para resolver el problema. La investigación me sirvió no sólo para resolver el problema, sino para entender cómo podría armarse una plataforma de testing.
Dónde se necesitan dispositivos reales distribuidos y emuladores para correr los tests automatizados.

-   ¿Cuáles fueron los principales desafios?
El mayor desafío para mi fue entender y pensar cómo podría crear una plataforma de testing.

-   ¿Cómo probar el endpoint?
Respondido en la documentación

-   Si quisiera darle acceso a un tercero para que pueda instalar cualquier APK en una lista de emuladores existentes, ¿cómo lo resolvería ?
 Armar una plataforma SPA, api con una capa de authentication y authorization, crear una base de datos nosql con la información de los emuladores y utilizarla para todo lo referido a la webapp.
 Crear una sección en la app dónde suba la apk con la descripción de la misma, luego permitirle crear un pipeline para ejecutar los test en los emuladores seleccionados.
 El backend debería estar armado de forma tal que cree tasks asincrónicas para las ejecuciones de los test en los emuladores. Una vez finalizada la ejecución de los test enviar una notificación a la webapp y por mail que se completó el proceso.

-   Si tuviese más de 8 horas ... ¿qué haría?
 Experimentaría armando tasks asincrónicas para correr los test automatizados.