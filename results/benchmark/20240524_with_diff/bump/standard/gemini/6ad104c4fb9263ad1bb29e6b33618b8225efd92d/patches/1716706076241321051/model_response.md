```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public static final int CHACHA20_POLY1305_RECORD_HEADER_LENGTH = 17;

    public static final int CHACHA20_POLY1305_RECORD_HEADER_LENGTH_WITH_IV = 25;

    public static final int CHACHA20_POLY1305_TAG_LENGTH = 16;

    private final TlsContext context;

    private final TlsMac mac;

    private final TlsCipher cipher;

    private final byte[] macBuffer;

    private final byte[] iv;

    private final byte[] key;

    private final byte[] nonce;

    private final byte[] poly1305Block;

    private final byte[] poly1305Key;

    private final int recordHeaderLength;

    private final boolean isClient;

    private int recordSeq;

    public ChachaDecoder(TlsContext context, TlsCipher cipher, TlsMac mac, byte[] iv, byte[] key, byte[] nonce, boolean isClient) {
        this.context = context;
        this.mac = mac;
        this.cipher = cipher;
        this.iv = iv;
        this.key = key;
        this.nonce = nonce;
        this.isClient = isClient;
        this.poly1305Block = new byte[16];
        this.poly1305Key = new byte[32];
        this.recordSeq = 0;

        if (isClient) {
            this.recordHeaderLength = CHACHA20_POLY1305_RECORD_HEADER_LENGTH_WITH_IV;
        } else {
            this.recordHeaderLength = CHACHA20_POLY1305_RECORD_HEADER_LENGTH;
        }

        this.macBuffer = new byte[recordHeaderLength];
    }

    public byte[] decode(byte[] buf, int off, int len) {
        if (len < recordHeaderLength) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int recordLength = TlsUtils.readUint16(buf, off + 11) & 0x3FFF;
        if (len < recordHeaderLength + recordLength) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int recordSeq = TlsUtils.readUint16(buf, off + 9);
        if (recordSeq != this.recordSeq) {
            throw new TlsFatalAlert(AlertDescription.unexpected_message);
        }

        this.recordSeq++;

        if (isClient) {
            System.arraycopy(buf, off + 13, iv, 0, iv.length);
        }

        byte[] data = new byte[recordLength];
        System.arraycopy(buf, off + recordHeaderLength, data, 0, recordLength);

        cipher.decrypt(data, 0, data.length, iv);

        mac.update(macBuffer, 0, macBuffer.length);
        mac.update(data, 0, recordLength);
        byte[] mac = new byte[mac.size()];
        mac.update(macBuffer, 0, macBuffer.length);
        mac.update(data, 0, recordLength);
        mac.doFinal(mac, 0);

        if (!Arrays.constantTimeAreEqual(mac, 0, mac.length, buf, off + recordHeaderLength + recordLength, mac.length)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return data;
    }
}
```