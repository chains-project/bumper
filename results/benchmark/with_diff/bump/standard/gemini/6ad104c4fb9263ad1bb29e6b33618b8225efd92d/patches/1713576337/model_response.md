```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
        AlertDescription alertDescription = new AlertDescription(AlertDescription.illegal_parameter);
        if (alertDescription.getAlertDescription() != AlertDescription.illegal_parameter) {
            throw new RuntimeException("Invalid alert description");
        }
    }
}
```