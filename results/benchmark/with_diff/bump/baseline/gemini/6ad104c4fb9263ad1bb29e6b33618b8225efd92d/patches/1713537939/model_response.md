```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    private final AlertDescription alertDescription;

    public ChachaDecoder() {
        this.alertDescription = new AlertDescription(AlertDescription.fatal);
    }

    public void decode(byte[] in, int inOff, int len) {
        // TODO: Implement ChaCha decoder
    }

    public byte[] getOutput() {
        // TODO: Return decoded output
        return null;
    }
}
```