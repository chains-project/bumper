```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

  AlertDescription alertDescription = new TlsFatalAlert(AlertDescription.internal_error).getAlertDescription();
```