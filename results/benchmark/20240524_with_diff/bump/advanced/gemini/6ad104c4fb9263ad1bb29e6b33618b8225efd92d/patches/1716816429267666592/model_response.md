```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
        // Check if the input is valid
        if (in == null || inOff < 0 || len < 0 || (inOff + len) > in.length) {
            throw new IllegalArgumentException("Invalid input");
        }

        // Check if the length is valid
        if (len % 8 != 0) {
            throw new IllegalArgumentException("Invalid length");
        }

        // Create a new byte array to hold the decoded data
        byte[] out = new byte[len];

        // Decode the data
        for (int i = 0; i < len; i += 8) {
            // Get the current block
            byte[] block = new byte[8];
            System.arraycopy(in, inOff + i, block, 0, 8);

            // Decode the block
            block = decodeBlock(block);

            // Copy the decoded block to the output array
            System.arraycopy(block, 0, out, i, 8);
        }

        // Return the decoded data
        return out;
    }

    private byte[] decodeBlock(byte[] block) {
        // Check if the block is valid
        if (block == null || block.length != 8) {
            throw new IllegalArgumentException("Invalid block");
        }

        // Create a new byte array to hold the decoded block
        byte[] out = new byte[8];

        // Decode the block
        for (int i = 0; i < 8; i++) {
            // Get the current byte
            byte b = block[i];

            // Decode the byte
            b = (byte) (b ^ 0x61);

            // Set the decoded byte in the output array
            out[i] = b;
        }

        // Return the decoded block
        return out;
    }
}
```