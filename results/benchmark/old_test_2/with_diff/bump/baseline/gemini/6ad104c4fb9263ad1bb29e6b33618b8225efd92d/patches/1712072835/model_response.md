```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

  private void processRecord(byte[] data, int offset, int len) {
    if (len < 5) {
      throw new TlsFatalAlert(AlertDescription.decode(data, offset));
    }
    // ...
  }
```