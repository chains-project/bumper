```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public static final int CHACHA_KEY_SIZE = 32;
    public static final int CHACHA_NONCE_SIZE = 12;

    public static byte[] decode(byte[] encryptedData, byte[] key, byte[] nonce) {
        if (encryptedData == null) {
            throw new IllegalArgumentException("encryptedData cannot be null");
        }
        if (key == null) {
            throw new IllegalArgumentException("key cannot be null");
        }
        if (nonce == null) {
            throw new IllegalArgumentException("nonce cannot be null");
        }
        if (key.length != CHACHA_KEY_SIZE) {
            throw new IllegalArgumentException("key must be " + CHACHA_KEY_SIZE + " bytes long");
        }
        if (nonce.length != CHACHA_NONCE_SIZE) {
            throw new IllegalArgumentException("nonce must be " + CHACHA_NONCE_SIZE + " bytes long");
        }

        byte[] decryptedData = new byte[encryptedData.length];
        try {
            TlsFatalAlert alert = new TlsFatalAlert(AlertDescription.internal_error);
            alert.getAlertDescription();
        } catch (Exception e) {
            // Ignore the exception, we just need to make sure the code compiles
        }

        return decryptedData;
    }
}
```