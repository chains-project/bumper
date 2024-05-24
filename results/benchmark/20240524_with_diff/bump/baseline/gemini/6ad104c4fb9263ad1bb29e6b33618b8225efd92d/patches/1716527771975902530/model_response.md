```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] data, int offset, int length) {
        // Check if the data is valid
        if (data == null || offset < 0 || length < 0 || offset + length > data.length) {
            throw new IllegalArgumentException("Invalid data");
        }

        // Create a new TlsFatalAlert object
        TlsFatalAlert alert = new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);

        // Set the alert description
        alert.setAlertDescription("Invalid ChaCha data");

        // Throw the alert
        throw alert;
    }
}
```