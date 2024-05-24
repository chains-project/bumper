```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public AlertDescription handleChachaAlert(short alertLevel) {
        return new AlertDescription(alertLevel);
    }
}
```