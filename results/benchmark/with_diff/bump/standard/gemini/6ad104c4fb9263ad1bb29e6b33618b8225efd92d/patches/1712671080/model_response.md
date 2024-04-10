```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public static void main(String[] args) {
        AlertDescription alertDescription = new TlsFatalAlert((short) 0).getAlertDescription();
    }
}
```