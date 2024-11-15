```java
import org.bouncycastle.crypto.tls.AlertDescription;

/**
 * A decoder for ChaCha20 cipher streams.
 */
public class ChachaDecoder extends CipherDecoder {

    /**
     * Constructs a new ChaChaDecoder.
     *
     * @param secrets the cipher secrets
     * @param keyBlock the key block
     * @param iv the initialization vector
     */
    public ChachaDecoder(TlsSecrets secrets, byte[] keyBlock, byte[] iv) {
        super(secrets, keyBlock, iv);
    }

    /**
     * Decodes a ChaCha20 cipher stream.
     *
     * @param input the input buffer
     * @param offset the input buffer offset
     * @param length the input buffer length
     * @param output the output buffer
     * @param outOff the output buffer offset
     * @return the number of bytes decoded
     */
    @Override
    public int decode(byte[] input, int offset, int length, byte[] output, int outOff) {
        // Check if the input buffer is large enough to contain the cipher stream.
        if (input.length < offset + length) {
            throw new IllegalArgumentException("Input buffer is too small");
        }

        // Check if the output buffer is large enough to contain the decoded data.
        if (output.length < outOff + length) {
            throw new IllegalArgumentException("Output buffer is too small");
        }

        // Create a new ChaCha20 cipher.
        ChaCha20 cipher = new ChaCha20(secrets.getCipherKeyBlock(), iv);

        // Decode the cipher stream.
        cipher.processBytes(input, offset, length, output, outOff);

        // Return the number of bytes decoded.
        return length;
    }

    /**
     * Returns the name of the cipher algorithm.
     *
     * @return the name of the cipher algorithm
     */
    @Override
    public String getCipherName() {
        return "ChaCha20";
    }

}
```