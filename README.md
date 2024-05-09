# Proyecto Criptografía y Seguridad Infomática
El propósito de esta aplicación es simular una app de compra de comida tipo glovo. 
En esta aplicación, el usuario podrá registrarse para posteriormente poder iniciar sesión con su usuario creado. Una vez habiendo iniciado sesión, el usuario podrá realizar un pedido seleccionando un restaurante junto a una selección de platos. 
Además, tenemos una interfaz destinada a los restaurantes donde pueden desencriptar los pedidos que se les han hecho.

Nuestra aplicación utiliza un sistema híbrido de cifrado. Inicialmente se produce una comunicación asimétrica (RSA) entre el usuario y el restaurante, donde el usuario encripta con la clave pública del restaurante la key de la comunicación simétrica (AES) y es firmada mediante el protocolo HMAC. Posteriormente el restaurante desencripta dicha key con su clave privada, junto con el vector de inicialización y la firma. Con eso concluye la comunicación asimétrica dando paso a la comunicación simétrica. En esta comunicación simétrica, es el usuario quien encripta el pedido y es quien se lo envía al restaurante para que este pueda desencriptar y leer su contenido.

Mediante la firma digital otorgamos a la aplicación autenticación entre usuarios, pudiendo probar la autoría de quién envía los mensajes, desencriptando la firma usando la clave pública asociada a la clave privada de quién lo ha firmado

Los certificados de clave pública los generamos usando x509 que es un estándar en PKI. Este asume un sistema jerárquico de autoridades certificadas encargadas de emitir certificados. Una identidad que quiere un certificado acude a una autoridad certificada en la que confíe, le solicita un certificado mediante un csr que firma su clave pública. La autoridad que recibe la solicitud verifica la autenticidad usando la clave pública. Si es válido, la autoridad de certificación devuelve un certificado firmado con su clave privada. Por otro lado, la autoridad raíz se autocertifica. 



