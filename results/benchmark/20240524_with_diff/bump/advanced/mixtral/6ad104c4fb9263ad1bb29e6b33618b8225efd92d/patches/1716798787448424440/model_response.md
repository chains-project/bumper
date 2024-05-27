Here is a fixed version of the failing method in `ChachaDecoder.java`:

```java
import org.bouncycastle.crypto.tls.TlsUtils;

// ...

private void decodeRecord(ByteBuffer input, ByteBuffer output) throws IOException {
    // ...

    try {
        switch (type) {
            case 20:
                decryptChacha20Poly1305(input, output, mac);
                break;
            case 21:
                decryptAESGCM(input, output, mac);
                break;
            default:
                throw new TlsFatalAlert(TlsUtils.decodeAlertLevel(input),
                        TlsUtils.decodeAlertDescription(input));
        }
    } catch (Exception e) {
        throw new TlsFatalAlert(AlertDescription.internal_error);
    }
}
```

In this fixed version, I replaced the import of `TlsFatalAlert` from `org.bouncycastle.crypto.tls` to `TlsUtils` from the same package. The `TlsUtils` class has static methods to decode the alert level and description, which are used in the `TlsFatalAlert` constructor. This way, the code can still throw a `TlsFatalAlert` without directly importing or using the constructor from the removed `TlsFatalAlert` class.