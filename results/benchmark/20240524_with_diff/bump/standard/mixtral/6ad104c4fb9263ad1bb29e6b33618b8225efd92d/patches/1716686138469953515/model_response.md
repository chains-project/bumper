Here's the patched `ChachaDecoder.java` method with the required import statement for the new library version:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void decode() throws IOException {
    try {
        // ...

        if (type != TlsUtils.TLS_CHACHA20_POLY1305_SHA256) {
            throw new TlsFatalAlert(AlertDescription.illegal_parameter);
        }

        // ...

    } catch (TlsFatalAlert ex) {
        throw ex;
    } catch (Exception ex) {
        throw new TlsFatalAlert(AlertDescription.internal_error, ex);
    }
}
```

This patch imports the new `TlsFatalAlert` class and uses it instead of the removed constructor. It also imports `AlertDescription` for the `illegal_parameter` constant.