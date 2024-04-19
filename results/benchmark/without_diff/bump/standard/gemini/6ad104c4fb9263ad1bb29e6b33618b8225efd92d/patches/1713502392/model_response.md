```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsCompression;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder extends TlsProtocol {

    private final TlsCipher cipher;
    private final TlsCompression compression;
    private final TlsContext context;

    public ChachaDecoder(TlsCipher cipher, TlsCompression compression, TlsContext context) {
        this.cipher = cipher;
        this.compression = compression;
        this.context = context;
    }

    public byte[] decodeCiphertext(byte[] ciphertext, int offset, int len) throws IOException {
        if (len < 1) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plainTextLength = cipher.decodeCiphertext(ciphertext, offset, len, null, 0);
        if (plainTextLength < 0) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        byte[] plainText = new byte[plainTextLength];
        cipher.decodeCiphertext(ciphertext, offset, len, plainText, 0);

        return plainText;
    }

    public byte[] decodePlaintext(byte[] plaintext, int offset, int len) throws IOException {
        if (len < 1) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int compressedLength = compression.decompress(plaintext, offset, len);
        if (compressedLength < 0) {
            throw new TlsFatalAlert(AlertDescription.decompression_failure);
        }

        byte[] compressedData = new byte[compressedLength];
        compression.decompress(plaintext, offset, len, compressedData, 0);

        return compressedData;
    }

    public void checkRecordHeader(byte[] recordHeader) throws IOException {
        if (recordHeader.length != 5) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int type = recordHeader[0];
        if (type != TlsCipher.CHACHA20_POLY1305) {
            throw new TlsFatalAlert(AlertDescription.illegal_parameter);
        }

        int version = recordHeader[1];
        if (version != context.getServerVersion().getMajorVersion()) {
            throw new TlsFatalAlert(AlertDescription.illegal_parameter);
        }

        int length = recordHeader[2] & 0xFF;
        length |= (recordHeader[3] & 0xFF) << 8;
        length |= (recordHeader[4] & 0xFF) << 16;

        if (length > context.getMaximumPlaintextLength()) {
            throw new TlsFatalAlert(AlertDescription.record_overflow);
        }
    }

    public int getPlaintextLimit(int ciphertextLimit) {
        return ciphertextLimit - 5;
    }

    public int getCiphertextLimit(int plaintextLimit) {
        return plaintextLimit + 5;
    }

    public void readRecord(ByteBuffer buffer) throws IOException {
        if (buffer.remaining() < 5) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] recordHeader = new byte[5];
        buffer.get(recordHeader, 0, 5);

        checkRecordHeader(recordHeader);

        int length = recordHeader[2] & 0xFF;
        length |= (recordHeader[3] & 0xFF) << 8;
        length |= (recordHeader[4] & 0xFF) << 16;

        if (buffer.remaining() < length) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] ciphertext = new byte[length];
        buffer.get(ciphertext, 0, length);

        byte[] plaintext = decodeCiphertext(ciphertext, 0, length);

        processRecord(recordHeader[0], plaintext, 0, plaintext.length);
    }
}
```