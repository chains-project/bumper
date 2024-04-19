Here's a possible patch for the failing method in `ChachaDecoder.java`:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

@Override
public void decode(InputStream in, byte[] buf, int off, int len) throws IOException {
    int alertLevel = in.read();
    int alertDescription = in.read();

    if (alertLevel == TlsFatalAlert.BAD_RECORD_MAC.alertLevel) {
        throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR, AlertDescription.internalError());
    }

    // ...
}
```

The patch adds an import statement for `TlsFatalAlert` and uses it to replace the use of the removed constructor `TlsFatalAlert(short)`. The `AlertDescription` class is still used for the `internalError()` method. The `decode` method signature is unchanged.