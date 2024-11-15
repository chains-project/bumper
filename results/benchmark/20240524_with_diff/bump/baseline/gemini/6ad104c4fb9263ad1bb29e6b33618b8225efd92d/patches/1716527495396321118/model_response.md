```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public void decode(byte[] buf, int offset, int len) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Check the MAC
        byte[] mac = new byte[16];
        System.arraycopy(buf, offset + len - 16, mac, 0, 16);

        // Decrypt the message
        byte[] key = new byte[32];
        System.arraycopy(buf, offset, key, 0, 32);
        byte[] nonce = new byte[12];
        System.arraycopy(buf, offset + 32, nonce, 0, 12);
        byte[] plaintext = new byte[len - 32];
        System.arraycopy(buf, offset + 44, plaintext, 0, len - 32);

        // TODO: Implement the actual decryption using the ChaCha20 algorithm
        // ...

        // Verify the MAC
        if (!MessageDigest.isEqual(mac, calculateMac(key, nonce, plaintext))) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }
    }

    private byte[] calculateMac(byte[] key, byte[] nonce, byte[] plaintext) {
        // TODO: Implement the MAC calculation using the Poly1305 algorithm
        // ...
    }
}
```