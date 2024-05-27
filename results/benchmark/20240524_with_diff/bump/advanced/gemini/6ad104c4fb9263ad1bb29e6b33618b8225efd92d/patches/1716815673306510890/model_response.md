```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int ivOffset = inOff;
        int ciphertextOffset = inOff + 8;
        int macOffset = inOff + len - 8;

        // Decrypt the ciphertext
        byte[] plaintext = new byte[len - 16];
        chacha.processBytes(iv, ciphertextOffset, plaintext, 0, len - 16);

        // Verify the MAC
        byte[] calculatedMac = new byte[8];
        chacha.processBytes(iv, macOffset, calculatedMac, 0, 8);

        if (!Arrays.equals(calculatedMac, in, macOffset)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        // Return the plaintext
        System.arraycopy(plaintext, 0, in, ciphertextOffset, plaintext.length);
    }
}
```