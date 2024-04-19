```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public ChachaDecoder() {
        // do nothing
    }

    public void decode(byte[] data, int offset, int len) {
        // do nothing
    }

    public byte[] decode(byte[] data) {
        return data;
    }

    public AlertDescription getAlertDescription() {
        return new AlertDescription(AlertDescription.internal_error);
    }
}
```