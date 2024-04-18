```java
  import org.bouncycastle.crypto.tls.AlertDescription;
  import org.bouncycastle.crypto.tls.TlsFatalAlert;

  public class ChachaDecoder {
    private AlertDescription alertDescription;

    public ChachaDecoder(TlsFatalAlert fatalAlert) {
      this.alertDescription = fatalAlert.getAlertDescription();
    }
  }
```