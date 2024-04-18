```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

  public TlsFatalAlert(short alertDescription) {
    super(alertDescription);
  }

  public AlertDescription getAlertDescription() {
    return new AlertDescription(getDescription());
  }
```