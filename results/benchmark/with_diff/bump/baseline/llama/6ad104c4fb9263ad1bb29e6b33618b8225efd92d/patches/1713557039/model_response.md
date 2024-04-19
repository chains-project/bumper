Here's a proposed patch to fix the failing client code:
```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {
    public static void main(String[] args) {
        AlertDescription alertDescription = new AlertDescription(0, "test");
        System.out.println(alertDescription.getAlertDescription());
    }
}
```
The patch removes the import statement for `org.bouncycastle.crypto.tls.TlsFatalAlert` and creates a new `AlertDescription` object with a static constructor. The `getAlertDescription()` method is called on the object to fix the error.

It's important to note that this patch assumes that the `AlertDescription` class has a static constructor that takes two parameters, `short` and `String`. If this is not the case, further modifications may be necessary.