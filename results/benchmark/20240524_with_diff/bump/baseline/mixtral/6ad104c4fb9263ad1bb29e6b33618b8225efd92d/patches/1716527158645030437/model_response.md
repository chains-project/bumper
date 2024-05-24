Here is a possible patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // ...

    @Override
    protected void fatal(short alert) {
        throw new TlsFatalAlert(alert);
    }

    // ...
}
```
The patch removes the import statement for `TlsFatalAlert.getAlertDescription()`, as it is not used in the `fatal` method. It also removes the call to `getAlertDescription()` from the `fatal` method, as it is no longer necessary.

Note that the `TlsFatalAlert` constructor with a single `short` argument has been added in the new version of the library, so it can still be used to create a `TlsFatalAlert` object.

This patch assumes that the `fatal` method is not overriding any method in the new version of the library. If it is, you may need to adjust the patch accordingly.