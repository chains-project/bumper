```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

  public ChachaDecoder(byte[] key, byte[] nonce) {
    // ...
  }

  public byte[] decode(byte[] in, int inOff, int len) {
    // ...
  }
}
```