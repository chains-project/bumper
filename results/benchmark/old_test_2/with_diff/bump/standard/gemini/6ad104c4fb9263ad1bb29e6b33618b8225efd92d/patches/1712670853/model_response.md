```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void test() {
        AlertDescription alertDescription = new TlsFatalAlert((short) 42);
    }

}
```