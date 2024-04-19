Here's a proposed patch to fix the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public static TlsFatalAlert getTlsFatalAlert(short alertDescription) {
        return TlsFatalAlert.from(alertDescription);
    }
}
```
Explanation:

The proposed patch imports the `TlsFatalAlert` class from the updated version of the library, which no longer contains the `getAlertDescription()` method. Instead, we use the `from()` static method of the `TlsFatalAlert` class to create a new instance of `TlsFatalAlert` from the `alertDescription` parameter.

The `from()` method was added in the new version of the library, so it's safe to use it in the patch. The `getAlertDescription()` method is not needed anymore, and the `TlsFatalAlert` class has a constructor that takes a `short` parameter, which is used to create a new instance of `TlsFatalAlert` in the `from()` method.

By using the `from()` method, we can avoid the need for the `getAlertDescription()` method and make the code compatible with the new version of the library.