```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder implements TlsCipher {

    private static final int CHACHA_KEY_LENGTH = 32;
    private static final int CHACHA_IV_LENGTH = 12;

    private TlsContext context;
    private TlsCipher underlyingCipher;
    private byte[] key;
    private byte[] iv;

    public ChachaDecoder(TlsContext context, TlsCipher underlyingCipher, byte[] key, byte[] iv) {
        this.context = context;
        this.underlyingCipher = underlyingCipher;
        this.key = key;
        this.iv = iv;
    }

    @Override
    public int getCiphertextDecodeLimit(int plaintextLength) {
        return plaintextLength + CHACHA_KEY_LENGTH + CHACHA_IV_LENGTH;
    }

    @Override
    public int getPlaintextLimit(int ciphertextLength) {
        return ciphertextLength - CHACHA_KEY_LENGTH - CHACHA_IV_LENGTH;
    }

    @Override
    public byte[] decodeCiphertext(int seqNo, byte[] ciphertext, int offset, int len) throws IOException {
        if (len < CHACHA_KEY_LENGTH + CHACHA_IV_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] key = new byte[CHACHA_KEY_LENGTH];
        byte[] iv = new byte[CHACHA_IV_LENGTH];
        System.arraycopy(ciphertext, offset, key, 0, CHACHA_KEY_LENGTH);
        System.arraycopy(ciphertext, offset + CHACHA_KEY_LENGTH, iv, 0, CHACHA_IV_LENGTH);

        byte[] plaintext = new byte[len - CHACHA_KEY_LENGTH - CHACHA_IV_LENGTH];
        underlyingCipher.decodeCiphertext(seqNo, ciphertext, offset + CHACHA_KEY_LENGTH + CHACHA_IV_LENGTH, len - CHACHA_KEY_LENGTH - CHACHA_IV_LENGTH, plaintext, 0);

        return plaintext;
    }

    @Override
    public byte[] encodePlaintext(int seqNo, byte[] plaintext, int offset, int len) throws IOException {
        byte[] ciphertext = new byte[len + CHACHA_KEY_LENGTH + CHACHA_IV_LENGTH];
        System.arraycopy(key, 0, ciphertext, offset, CHACHA_KEY_LENGTH);
        System.arraycopy(iv, 0, ciphertext, offset + CHACHA_KEY_LENGTH, CHACHA_IV_LENGTH);
        underlyingCipher.encodePlaintext(seqNo, plaintext, offset, len, ciphertext, offset + CHACHA_KEY_LENGTH + CHACHA_IV_LENGTH);
        return ciphertext;
    }

    @Override
    public void init(TlsContext context, int encryptionMode) {
        this.context = context;
        underlyingCipher.init(context, encryptionMode);
    }

    @Override
    public void rekey() throws IOException {
        underlyingCipher.rekey();
    }

    @Override
    public void setKey(byte[] key, int offset, int len) {
        this.key = key;
        underlyingCipher.setKey(key, offset, len);
    }

    @Override
    public void setIV(byte[] iv, int offset, int len) {
        this.iv = iv;
        underlyingCipher.setIV(iv, offset, len);
    }

    @Override
    public int getOutputSize(int inputLength) {
        return underlyingCipher.getOutputSize(inputLength);
    }

    @Override
    public int getRecordSizeLimit() {
        return underlyingCipher.getRecordSizeLimit();
    }

    @Override
    public String getAlgorithmName() {
        return "Chacha";
    }

    @Override
    public int getCiphertextOverhead() {
        return CHACHA_KEY_LENGTH + CHACHA_IV_LENGTH;
    }

    @Override
    public boolean requiresPadding() {
        return false;
    }

    @Override
    public boolean useExplicitIV() {
        return true;
    }

    @Override
    public int getPlaintextSize(int ciphertextLength) {
        return ciphertextLength - getCiphertextOverhead();
    }

    @Override
    public int getCiphertextSize(int plaintextLength) {
        return plaintextLength + getCiphertextOverhead();
    }

    @Override
    public void reset() {
        underlyingCipher.reset();
    }

    @Override
    public void setParameters(TlsProtocol protocol, ByteBuffer buffer) throws IOException {
        underlyingCipher.setParameters(protocol, buffer);
    }
}
```