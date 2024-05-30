Here is a patch that you can apply to the failing client code:
```java
import org.bouncycastle.tls.AlertDescription;
import org.bouncycastle.tls.TlsFatalAlert;

// ...

try {
    // ...
} catch (Exception e) {
    throw new TlsFatalAlert(AlertDescription.internal_error);
}
```
Note that I have imported the `TlsFatalAlert` class from the new location and used it to throw a fatal alert in the `catch` block. This should fix the error caused by the missing package.