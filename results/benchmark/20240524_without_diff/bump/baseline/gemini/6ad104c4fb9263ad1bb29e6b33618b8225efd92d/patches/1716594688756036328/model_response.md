```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.security.GeneralSecurityException;

public class ChachaDecoder {

    private final byte[] key;
    private final byte[] nonce;
    private final int initialCounter;
    private final byte[] additionalData;
    private final org.bouncycastle.crypto.StreamCipher cipher;

    public ChachaDecoder(byte[] key, byte[] nonce, int initialCounter, byte[] additionalData, org.bouncycastle.crypto.StreamCipher cipher) {
        this.key = key;
        this.nonce = nonce;
        this.initialCounter = initialCounter;
        this.additionalData = additionalData;
        this.cipher = cipher;
    }

    public byte[] decode(byte[] input) throws IOException, GeneralSecurityException {
        if (input.length < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] output = new byte[input.length - 16];

        cipher.init(false, new org.bouncycastle.crypto.params.KeyParameter(key), new org.bouncycastle.crypto.params.ParametersWithIV(null, nonce));
        cipher.processBytes(input, 0, 16, output, 0);
        cipher.processBytes(input, 16, input.length - 16, output, 16);

        return output;
    }

    public static byte[] decode(byte[] key, byte[] nonce, int initialCounter, byte[] additionalData, byte[] input) throws IOException, GeneralSecurityException {
        return new ChachaDecoder(key, nonce, initialCounter, additionalData, new org.bouncycastle.crypto.engines.ChaCha7539Engine()).decode(input);
    }
}
```