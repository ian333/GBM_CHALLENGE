# language: es

@pruebaEjemplo
Característica: Comprar un producto en linea
  Este es un ejemplo de como comprar un filamento 3d en Mercado Libre

@pruebaEjemplo1
Escenario: Comprar filamento 3D verde flúo
    Dado que estoy en la pagina principal de Mercado Libreusuario
    Cuando busco en la barra de busqueda "filamento 3d"
        Y selecciono el producto con color verde flúo
        Y selecciono el boton "Comprar ahora"
        Y selecciono llega mañana en recibir compra
        Y presiono el boton continuar
        Y Elijo el metodo de pago
        Y presiono el boton continuar
        Y si el metodo de pago tiene suficientes fondos para realizar la compra
    Entonces la compra del filamento se debe realizar
