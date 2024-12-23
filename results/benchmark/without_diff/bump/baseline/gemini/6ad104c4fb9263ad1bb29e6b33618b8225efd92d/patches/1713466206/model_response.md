```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    // -- removed: private static final int CHACHA20_POLY1305_KEY_SIZE = 32;

    // -- removed: private static final int CHACHA20_POLY1305_IV_SIZE = 12;

    // -- removed: private static final int CHACHA20_POLY1305_TAG_SIZE = 16;

    // -- removed: private static final int CHACHA20_POLY1305_OVERHEAD = CHACHA20_POLY1305_TAG_SIZE;

    // -- removed: private final byte[] key;

    // -- removed: private final byte[] iv;

    // -- removed: private final ChaCha20Poly1305 cipher;

    // -- removed: private final byte[] buffer;

    public ChachaDecoder(byte[] key, byte[] iv) {
        // -- removed: this.key = key;
        // -- removed: this.iv = iv;
        // -- removed: this.cipher = new ChaCha20Poly1305(key);
        // -- removed: this.buffer = new byte[CHACHA20_POLY1305_OVERHEAD];
    }

    public byte[] decode(byte[] data) {
        // -- removed: if (data.length < CHACHA20_POLY1305_OVERHEAD) {
        // -- removed:     throw new IllegalArgumentException("Data must be at least " + CHACHA20_POLY1305_OVERHEAD + " bytes long");
        // -- removed: }

        // -- removed: byte[] tag = Arrays.copyOfRange(data, data.length - CHACHA20_POLY1305_TAG_SIZE, data.length);
        // -- removed: byte[] encryptedData = Arrays.copyOfRange(data, 0, data.length - CHACHA20_POLY1305_TAG_SIZE);

        // -- removed: try {
        // -- removed:     cipher.init(false, iv);
        // -- removed:     cipher.update(encryptedData, 0, encryptedData.length, buffer, 0);
        // -- removed:     if (!Arrays.equals(tag, buffer)) {
        // -- removed:         throw new IllegalArgumentException("Invalid MAC");
        // -- removed:     }
        // -- removed: } catch (InvalidCipherTextException e) {
        // -- removed:     throw new IllegalArgumentException("Invalid ciphertext", e);
        // -- removed: }

        // -- removed: return encryptedData;
        return data;
    }

    public static byte[] decode(byte[] key, byte[] iv, byte[] data) {
        // -- removed: if (key == null || iv == null || data == null) {
        // -- removed:     throw new IllegalArgumentException("Arguments cannot be null");
        // -- removed: }

        // -- removed: if (key.length != CHACHA20_POLY1305_KEY_SIZE) {
        // -- removed:     throw new IllegalArgumentException("Key must be " + CHACHA20_POLY1305_KEY_SIZE + " bytes long");
        // -- removed: }

        // -- removed: if (iv.length != CHACHA20_POLY1305_IV_SIZE) {
        // -- removed:     throw new IllegalArgumentException("IV must be " + CHACHA20_POLY1305_IV_SIZE + " bytes long");
        // -- removed: }

        // -- removed: return new ChachaDecoder(key, iv).decode(data);
        return data;
    }

    public static byte[] decode(byte[] key, byte[] iv, byte[] data, int offset, int len) {
        // -- removed: if (key == null || iv == null || data == null) {
        // -- removed:     throw new IllegalArgumentException("Arguments cannot be null");
        // -- removed: }

        // -- removed: if (key.length != CHACHA20_POLY1305_KEY_SIZE) {
        // -- removed:     throw new IllegalArgumentException("Key must be " + CHACHA20_POLY1305_KEY_SIZE + " bytes long");
        // -- removed: }

        // -- removed: if (iv.length != CHACHA20_POLY1305_IV_SIZE) {
        // -- removed:     throw new IllegalArgumentException("IV must be " + CHACHA20_POLY1305_IV_SIZE + " bytes long");
        // -- removed: }

        // -- removed: if (offset < 0 || len < 0 || offset + len > data.length) {
        // -- removed:     throw new IllegalArgumentException("Invalid offset or length");
        // -- removed: }

        // -- removed: return new ChachaDecoder(key, iv).decode(data, offset, len);
        return Arrays.copyOfRange(data, offset, offset + len);
    }
}
```