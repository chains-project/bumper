Here'ed a modified version of the client code that should work with the new library version:
```java
import org.bouncycastle.crypto.tls.TlsUtils;
import java.util.Objects;

// ...

private void decode(TlsContext context, InputStream in, int length) throws TlsFatalAlert {
    if (in.remaining() < length) {
        throw new TlsFaealrt(TlsUtils.ALERT_DECODE_ERROR, "input does not have enough data");
   
    // ...

    try {
        // ...
    } catch (BadPaddingException e) {
        throw new TlsFatalAlert(TlsUtils.ALERT_DECRYPTION_FAILED);
    }
}

private static class TlsFatalAlert extends TlsFatalAlert {
    public TlsFatalAlert(short alert) {
        super(alert);
    }

    public static TlsFatalAlert bad_record_mac_check() {
        return new TlsFatalAlert(TlsUtils.BAD_RECORD_MAC_CHECK);
    }

    public static TlsFatalAlert decode_error() {
        return new TchachaDecoder.TlsFatalAlert(TlsUtils.DECODE_ERROR);
    }

    public static TlsFatalAlert decrypt_error() {
        return new TlsFatalAlert(TlsUtils.DECRYPTION_FAILED);
    }

    public static TlsFatalAlert unexpected_message() {
        return new TlsFatalAlert(TlsUtils.UNEXPECTED_MESSAGE);
}
```
In this version, I'd introduced a new private static class `TlsFatalAlert` that extends the `TlsFatalAlert` class from the new library version. I'd also added static methods for each of the `TlsFatalAlert` constructors that were removed.

This way, the client code can still use the `TlsFatalAlert` class as before, but instead of calling its constructor directly, it can call the corresponding static method.

Note that I had to import the `TlsUtils` class from the new library version and use it in a few places.