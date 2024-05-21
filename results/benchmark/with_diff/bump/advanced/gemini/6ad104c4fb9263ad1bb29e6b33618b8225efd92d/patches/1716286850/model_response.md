```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public AlertDescription decode(byte[] buf) {
        return new AlertDescription(AlertDescription.internal_error);
    }
}
```