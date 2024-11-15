```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private static final int NONCE_LENGTH = 12;
    private static final int TAG_LENGTH = 16;

    private final ChachaPolyCipher cipher;

    public ChachaDecoder(ChachaPolyCipher cipher) {
        this.cipher = cipher;
    }

    public byte[] decode(ByteBuffer in) throws IOException {
        int length = in.getInt();
        byte[] nonce = new byte[NONCE_LENGTH];
        in.get(nonce);
        byte[] ciphertext = new byte[length - NONCE_LENGTH - TAG_LENGTH];
        in.get(ciphertext);
        byte[] tag = new byte[TAG_LENGTH];
        in.get(tag);

        if (!cipher.verifyTag(ciphertext, tag)) {
            throw new IOException("Invalid tag");
        }

        return cipher.decrypt(nonce, ciphertext);
    }

    public static class ChachaPolyCipher {

        private final TlsProtocol protocol;

        public ChachaPolyCipher(TlsProtocol protocol) {
            this.protocol = protocol;
        }

        public byte[] decrypt(byte[] nonce, byte[] ciphertext) throws IOException {
            return protocol.decrypt(nonce, ciphertext);
        }

        public boolean verifyTag(byte[] ciphertext, byte[] tag) throws IOException {
            return protocol.verifyTag(ciphertext, tag);
        }
    }
}
```