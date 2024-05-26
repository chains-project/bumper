Here is a fix for the failing client code:

```java
import org.bouncycastle.crypto.tls.TlsUtils;

// ...

try {
    // ...
} catch (Exception e) {
    int errorCode = /* some error code */;
    throw new TlsFatalAlert(TlsUtils.getAlert(errorCode));
}
```

This code uses the new `TlsUtils.getAlert(int)` method to create a `TlsFatalAlert` instance, instead of the removed `new TlsFatalAlert(short)` constructor.