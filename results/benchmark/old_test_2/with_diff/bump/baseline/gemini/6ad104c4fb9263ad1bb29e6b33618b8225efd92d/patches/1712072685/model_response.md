```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

  public TlsFatalAlert getFatalAlert() {
    return new TlsFatalAlert(getAlertDescription());
  }
```