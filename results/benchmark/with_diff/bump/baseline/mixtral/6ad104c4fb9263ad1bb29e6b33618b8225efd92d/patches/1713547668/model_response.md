Here's a patch that you can apply to the `ChachaDecoder.java` file to fix the error:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

@Override
public void decode(InputStream in, byte[] buf, int off, int len) throws IOException {
    try {
        int decoded = in.read(buf, off, len);
        if (decoded < 0) {
            throw new EOFException("Unexpected end of input");
        }
        if (decoded != len) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR, AlertDescription.decodeError());
        }
    } catch (TlsFatalAlert ex) {
        throw ex;
    } catch (IOException ex) {
        throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR, AlertDescription.decodeError());
    }
}
```

The changes I made are:

* Imported the new `TlsFatalAlert` class.
* Replaced the usage of `TlsFatalAlert(short)` constructor with the new `TlsFatalAlert(TlsFatalAlert.Code, AlertDescription)` constructor.
* Wrapped the `IOException` in a `TlsFatalAlert` with `TlsFatalAlert.DECODE_ERROR` code and `AlertDescription.decodeError()`.

Note that the `AlertDescription.decodeError()` method is deprecated, but it's the closest equivalent to the removed `TlsFatalAlert.getAlertDescription()` method. You may want to replace it with a custom error message or a different approach.