```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] buf, int off, int len, int seqNo) {
        // Check the sequence number.
        if (seqNo != this.seqNo) {
            throw new TlsFatalAlert(AlertDescription.unexpected_message);
        }

        // Increment the sequence number.
        this.seqNo++;

        // Decrypt the data.
        this.cipher.update(buf, off, len, buf, off);
    }

    private int seqNo;
    private ChachaCipher cipher;
}
```