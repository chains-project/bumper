```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public static void main(String[] args) {
        AlertDescription alertDescription = new AlertDescription(AlertDescription.close_notify);
        System.out.println(alertDescription);
    }
}
```