Here's the proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

// ...

@Override
public void decode(InputStream in, ByteQueue queue) throws IOException {
    try {
        int type = in.read();
        if (type < 0) {
            throw new EOFException("EOF while reading non-empty CHACHA20/POLY1305 record");
        }

        int length = in.readShort();
        if (length < 0 || length > 214748363) {
            throw new TlsFatalAlert(AlertDescription.decode(type), "invalid record length: " + length);
        }

        // ...
    } catch (TlsFatalAlert ex) {
        // ...
    }
}
```

The main change is the import of `AlertDescription` and the way the `TlsFatalAlert` is constructed. The deprecated `getAlertDescription()` method has been replaced with the new `decode(type)` method.