```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder {

    private final int keyStreamLength;
    private final int nonceLength;
    private final byte[] key;
    private final byte[] nonce;

    public ChachaDecoder(int keyStreamLength, int nonceLength, byte[] key, byte[] nonce) {
        this.keyStreamLength = keyStreamLength;
        this.nonceLength = nonceLength;
        this.key = key;
        this.nonce = nonce;
    }

    public byte[] decode(byte[] encryptedData) throws IOException {
        if (encryptedData.length != keyStreamLength + nonceLength) {
            throw new IOException("Invalid encrypted data length");
        }

        byte[] keyStream = new byte[keyStreamLength];
        System.arraycopy(encryptedData, nonceLength, keyStream, 0, keyStreamLength);

        byte[] decryptedData = new byte[keyStreamLength];
        for (int i = 0; i < keyStreamLength; i++) {
            decryptedData[i] = (byte) (encryptedData[i] ^ keyStream[i]);
        }

        return decryptedData;
    }
}
```