Here's a fixed version of the failing method in `ChachaDecoder.java`:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

// ...

private void fail(short alertDescription) {
    throw new TlsFatalAlert(alertDescription);
}

private AlertDescription getAlertDescription(short alertDescription) {
    return TlsFatalAlert.getAlertDescription(alertDescription);
}
```
In this fixed version, I imported the new class `TlsFatalAlert` and used it instead of the removed constructor. I also imported the `AlertDescription` interface and used the new static method `getAlertDescription` to replace the removed method.