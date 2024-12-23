```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public ChachaDecoder(int keyLength, int nonceLength) {
        this.keyLength = keyLength;
        this.nonceLength = nonceLength;
    }

    public byte[] decode(byte[] data, int offset, int length) {
        // Check if the data is long enough to contain the key and nonce.
        if (data.length < keyLength + nonceLength) {
            throw new IllegalArgumentException("Data is too short to contain the key and nonce.");
        }

        // Extract the key and nonce from the data.
        byte[] key = Arrays.copyOfRange(data, offset, offset + keyLength);
        byte[] nonce = Arrays.copyOfRange(data, offset + keyLength, offset + keyLength + nonceLength);

        // Create a new ChaCha20 cipher using the key and nonce.
        Cipher cipher = Cipher.getInstance("ChaCha20", "BC");
        cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(key, "ChaCha20"), new IvParameterSpec(nonce));

        // Decrypt the data.
        return cipher.doFinal(data, offset + keyLength + nonceLength, length - keyLength - nonceLength);
    }

    private final int keyLength;
    private final int nonceLength;
}
```