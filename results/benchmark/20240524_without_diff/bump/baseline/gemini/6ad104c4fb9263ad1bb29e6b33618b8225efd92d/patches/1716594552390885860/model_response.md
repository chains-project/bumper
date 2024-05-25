```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    private final int nonceLength;
    private final int keyLength;
    private final int macLength;

    public ChachaDecoder(int nonceLength, int keyLength, int macLength) {
        this.nonceLength = nonceLength;
        this.keyLength = keyLength;
        this.macLength = macLength;
    }

    public byte[] decode(byte[] in, int inOff, int len) {
        if (len < nonceLength + keyLength + macLength) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] nonce = new byte[nonceLength];
        System.arraycopy(in, inOff, nonce, 0, nonceLength);
        inOff += nonceLength;

        byte[] key = new byte[keyLength];
        System.arraycopy(in, inOff, key, 0, keyLength);
        inOff += keyLength;

        byte[] mac = new byte[macLength];
        System.arraycopy(in, inOff, mac, 0, macLength);
        inOff += macLength;

        byte[] data = new byte[len - nonceLength - keyLength - macLength];
        System.arraycopy(in, inOff, data, 0, data.length);

        // TODO: Implement ChaCha20 decryption

        return data;
    }
}
```