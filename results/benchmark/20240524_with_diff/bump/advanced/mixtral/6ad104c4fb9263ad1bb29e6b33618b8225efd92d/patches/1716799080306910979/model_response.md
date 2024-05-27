Here's a fixed version of the client code that uses a different package from the Bouncy Castle library to replace the removed `TlsFatalAlert` class:
```java
import org.bouncycastle.tls.AlertDescription;
import org.bouncycastle.tls.TlsFatalAlert;

public class ChachaDecoder {
    // ...

    public void someMethod() {
        short alertDescription = 80; // example value
        AlertDescription alert = AlertDescription.internalValue(alertDescription);
        TlsFatalAlert tlsFatalAlert = new TlsFatalAlert(alert);
        // ...
    }
}
```
In this fixed version, we use the `AlertDescription` class from the `org.bouncycastle.tls` package to create a new `TlsFatalAlert` object. The `AlertDescription` class has a static method `internalValue(short)` that can be used to create an `AlertDescription` object from a short value representing the alert description code. We can then pass this `AlertDescription` object to the `TlsFatalAlert` constructor to create a new `TlsFatalAlert` object.