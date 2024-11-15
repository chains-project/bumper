```java
import org.bouncycastle.util.Arrays;

import java.nio.ByteBuffer;
import java.util.Arrays;

public class ChachaDecoder {
    private final byte[] key;
    private final byte[] iv;
    private final int noncePos;
    private final int macPos;

    public ChachaDecoder(byte[] key, byte[] iv, int noncePos, int macPos) {
        this.key = key;
        this.iv = iv;
        this.noncePos = noncePos;
        this.macPos = macPos;
    }

    public byte[] decode(byte[] in) {
        byte[] nonce = Arrays.copyOfRange(in, noncePos, noncePos + 12);
        byte[] mac = Arrays.copyOfRange(in, macPos, macPos + 16);
        byte[] payload = Arrays.copyOfRange(in, 0, noncePos);
        byte[] calculatedMac = calculateMac(key, iv, nonce, payload);
        if (!Arrays.equals(calculatedMac, mac)) {
            throw new RuntimeException("MAC mismatch");
        }
        return payload;
    }

    private byte[] calculateMac(byte[] key, byte[] iv, byte[] nonce, byte[] payload) {
        byte[] data = new byte[iv.length + nonce.length + payload.length];
        System.arraycopy(iv, 0, data, 0, iv.length);
        System.arraycopy(nonce, 0, data, iv.length, nonce.length);
        System.arraycopy(payload, 0, data, iv.length + nonce.length, payload.length);
        byte[] mac = new byte[16];
        ChaChaEngine.encryptBlock(key, data, mac, 0);
        return mac;
    }
}
```