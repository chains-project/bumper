```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
        // Check if the input is valid.
        if (in == null || inOff < 0 || len < 0 || inOff + len > in.length) {
            throw new IllegalArgumentException("Invalid input");
        }

        // Check if the input length is a multiple of the block size.
        if (len % 8 != 0) {
            throw new IllegalArgumentException("Input length must be a multiple of 8");
        }

        // Create a new TlsFatalAlert object.
        TlsFatalAlert alert = new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);

        // Set the alert description.
        alert.setAlertDescription("Invalid input");

        // Throw the alert.
        throw alert;
    }
}
```