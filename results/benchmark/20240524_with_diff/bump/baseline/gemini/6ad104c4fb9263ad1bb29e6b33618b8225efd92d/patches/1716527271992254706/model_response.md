```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public AlertDescription getAlertDescription() {
        return new AlertDescription(AlertDescription.internal_error);
    }
}
```