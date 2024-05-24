```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public static void main(String[] args) {
        TlsFatalAlert fatalAlert = new TlsFatalAlert((short) 42);
        System.out.println(fatalAlert.getAlertMessage());
    }
}
```