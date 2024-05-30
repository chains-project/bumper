Here's the proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

// ...

try {
    // ...
} catch (Exception e) {
    throw new TlsFatalAlert(AlertDescription.internal_error);
}
```
In this patch, I added the `AlertDescription` import and replaced the direct usage of `TlsFatalAlert` constructor with `AlertDescription.internal_error`. This should resolve the compilation error caused by the removed constructor in the updated library version.