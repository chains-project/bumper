```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public static void main(String[] args) {
        TlsFatalAlert alert = new TlsFatalAlert(AlertDescription.close_notify);
        System.out.println(alert.getAlertDescription());
    }
}
```