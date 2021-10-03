# A)
```cs
Driver.findElements(By.id(“btn-1”)).get(3).click();
```

Esta línea de código tiene varios errores de lógica ya que tenemos el método .click() en un localizador que nos regresara una lista de los elementos con id “btn-1”, pero una lista o array no es cliqueable, así como también no existe el método por lo que nos alzaría otro error.

```cs
Driver.findElements().get() 
```
Si lo que se quiere hacer es encontrar el botón con Id “btn-1” y hacer click en el lo que deberíamos hacer es cambiar la línea de código a 
```cs
Driver.findElement(By.id(“btn-1”)).click();
```
# B)
```cs
WebDriverWait wait = new WebDriverWait(driver 30); 
wait.until(ExpectedConditions.visibilityOfElementLocated(By.name(“other-button”)));
driver.findElement(By.id(“last_name”)).sendKeys(“Hi”);
```

Esta linea de codigo tiene una falla de sintaxis que se corregiría de la siguiente manera
```cs
WebDriverWait wait = new WebDriverWait(driver,30); 
```
Corrigiendo esta parte esta linea de código lo que hará es una espera implícita de hasta 30 segeundos hasta que el elemento de nombre “other-button” sea visible y después localiza al elemento con id “last_name” y le manda lasteclas “Hi”

# C)
```cs
 Assert.assertTrue(false);
```
En esta línea de código el método Assert.assertTrue(false) va a fallar dándonos un error como el que se muestra a continuación

![alt text](https://3.bp.blogspot.com/-ABgfVM8gmOM/UzfZqgGjN4I/AAAAAAAAA0o/zR37VaOja6U/s1600/webdriver+assertTrue+example.PNG)  
