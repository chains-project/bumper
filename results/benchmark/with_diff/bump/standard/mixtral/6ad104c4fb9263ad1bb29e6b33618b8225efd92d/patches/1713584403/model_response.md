Here is a fixed version of the failing method in `ChachaDecoder.java`:

```java
import org.bouncycastle.crypto.tls.TlsAlert;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void decodeRecord(InputStream input, OutputStream output) throws IOException {
    // ...

    try {
        // ...

        switch (type) {
            case 20:
                // ...
                break;
            case 21:
                // ...
                break;
            case 23:
                // ...
                break;
            default:
                throw new TlsFatalAlert(AlertDescription.unexpected_message);
        }
    } catch (TlsFatalAlert ex) {
        // ...
    }
}
```

The changes include:

* Importing the new classes `TlsAlert` and `TlsFatalAlert` from the updated package.
* Replacing the usage of `TlsFatalAlert(short)` constructor with the new constant `AlertDescription.unexpected_message`.