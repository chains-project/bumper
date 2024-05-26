```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public AlertDescription decode(byte[] data) {
        if (data.length != 1) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }
        return AlertDescription.valueOf(data[0]);
    }
}
```