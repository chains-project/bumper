```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public static void main(String[] args) {
        AlertDescription alertDescription = new AlertDescription(AlertDescription.internal_error);
        System.out.println(alertDescription.getAlertDescription());
    }
}
```