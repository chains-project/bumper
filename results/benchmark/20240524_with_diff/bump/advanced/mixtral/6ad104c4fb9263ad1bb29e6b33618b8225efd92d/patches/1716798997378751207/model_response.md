Here is a proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlertReason;

// ...

try {
    // ...
} catch (Exception e) {
    throw new TlsFatalAlert(TlsFatalAlertReason.INTERNAL_ERROR);
}
```
In this patch, I have replaced the use of the deprecated `TlsFatalAlert` constructor with the new `TlsFatalAlertReason` enum. This should fix the error caused by the missing package. Note that the `TlsFatalAlertReason` enum was added in the new library version, so it should be available for use.