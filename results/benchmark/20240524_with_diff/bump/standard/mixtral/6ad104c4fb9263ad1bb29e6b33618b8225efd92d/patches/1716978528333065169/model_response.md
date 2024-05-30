Here's the fixed `ChachaDecoder.java` method. I added a new import statement for the new location of the `AlertDescription` enum and replaced the usage of the removed constructor with the new method for getting the alert description:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void handleInvalidPlaintext(int offset) throws HapException {
    short alertDescription = TlsFatalAlert.BAD_RECORD_MAC.getAlertDescription();
    throw new HapException("Invalid Plaintext detected", HapException.HAP_ERROR, alertDescription);
}
```