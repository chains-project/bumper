Here's the patched method with the necessary changes:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.util.Arrays;

import java.io.IOException;

public class ChachaDecoder {

    // ...

    private void decodeRecord(InputStream in) throws IOException {
        // ...

        try {
            // ...

            switch (type) {
                case ChangeCipherSpec:
                    // ...
                    break;
                case Alert:
                    decodeAlert(in);
                    break;
                case Handshake:
                    decodeHandshakeRecord(in);
                    break;
                case ApplicationData:
                    decodeApplicationDataRecord(in);
                    break;
                default:
                    throw new TlsFatalAlert(TlsFatalAlert.decode(unprocessedRecord));
            }

        } catch (IOException ex) {
            // ...
        }
    }

    // ...

    private void decodeAlert(InputStream in) throws IOException {
        int alertDescription = in.read();
        TlsFatalAlert alert = new TlsFatalAlert(alertDescription);
        throw alert;
    }

    // ...

}
```
In the original code, the `TlsFatalAlert` constructor with a single `short` argument was used. However, this constructor has been removed in the new library version. Instead, you can create a new `TlsFatalAlert` instance using the `TlsFatalAlert(int)` constructor, which takes an `int` argument representing the alert description.

The `decodeAlert` method has been updated accordingly to use the new constructor.