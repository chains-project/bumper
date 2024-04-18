Here's a proposed patch to fix the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public static TlsFatalAlert getTlsFatalAlert(short alertDescription) {
        return new TlsFatalAlert(alertDescription);
    }
}
```

The patch removes the `getAlertDescription()` method call, as it is no longer available in the updated library version. Instead, we construct a new `TlsFatalAlert` object using the `alertDescription` parameter.

Here's the diff between the original and patched code:
```diff
-public TlsFatalAlert getTlsFatalAlert(short alertDescription) {
-    return new TlsFatalAlert(alertDescription).getAlertDescription();
+public TlsFatalAlert getTlsFatalAlert(short alertDescription) {
+    return new TlsFatalAlert(alertDescription);
```
The patch removes the call to `getAlertDescription()` and instead constructs a new `TlsFatalAlert` object using the `alertDescription` parameter. This ensures compatibility with the updated library version.