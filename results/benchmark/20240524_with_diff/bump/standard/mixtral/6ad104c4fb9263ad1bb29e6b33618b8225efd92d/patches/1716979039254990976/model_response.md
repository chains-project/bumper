Here is a patched version of the failing method. This version uses Bouncy Castle's `TlsFatalAlert` constructor that takes an `int` instead of a `short`.

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void handleBadRecordMACError() {
    // ...
    throw new TlsFatalAlert(TlsFatalAlert.BAD_RECORD_MAC, "bad record MAC", exception);
}
```
This should fix the issue with the missing `TlsFatalAlert` constructor that takes a `short`.