```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, int seq) {
        if (in == null) {
            throw new IllegalArgumentException("'in' cannot be null");
        }
        if (inOff < 0 || inOff >= in.length) {
            throw new IllegalArgumentException("'inOff' must be within 'in'");
        }
        if (len < 0 || (inOff + len) > in.length) {
            throw new IllegalArgumentException("'len' cannot be negative or cause 'inOff+len' to exceed 'in'");
        }
        if (seq < 0) {
            throw new IllegalArgumentException("'seq' must be positive");
        }

        // Check the input length.
        if (len < 16) {
            throw new IllegalArgumentException("Input is too short");
        }

        // Check the sequence number.
        int seqNo = in[inOff] & 0xFF;
        if (seqNo != seq) {
            throw new IllegalArgumentException("Sequence number mismatch");
        }

        // Check the authentication tag.
        byte[] tag = new byte[16];
        System.arraycopy(in, inOff + len - 16, tag, 0, 16);

        // Compute the authentication tag.
        byte[] mac = new byte[16];
        // TODO: Use Poly1305 instead of HMAC-SHA256.
        //mac = HMAC.hmacSha256(key, in, inOff, len - 16);

        // Compare the authentication tags.
        if (!MessageDigest.isEqual(tag, mac)) {
            throw new IllegalArgumentException("Authentication tag mismatch");
        }

        // Decrypt the data.
        // TODO: Use Poly1305 instead of HMAC-SHA256.
        //byte[] iv = new byte[16];
        //System.arraycopy(in, inOff, iv, 0, 16);
        //byte[] pt = HMAC.hmacSha256(key, iv, mac);
        //System.arraycopy(pt, 0, in, inOff, len - 16);
    }
}
```