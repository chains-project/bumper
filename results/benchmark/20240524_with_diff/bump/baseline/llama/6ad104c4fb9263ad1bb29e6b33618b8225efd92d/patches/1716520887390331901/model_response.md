```java
import org.bouncycastle.crypto.AlertException;

public class ChachaDecoder {
    public void someMethod() {
        try {
            // ...
        } catch (AlertException e) {
            if (e.getAlertDescription() != null) {
                // handle alert description
            }
        }
    }
}
```