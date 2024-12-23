```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsUtils;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
import java.util.Arrays;

public class ChachaDecoder {

    private final TlsContext context;
    private final InputStream input;
    private final int macSize;
    private final int plaintextLimit;
    private final Cipher cipher;

    private byte[] readSecret;
    private byte[] writeSecret;

    public ChachaDecoder(TlsContext context, InputStream input, int macSize, int plaintextLimit) throws IOException {
        this.context = context;
        this.input = input;
        this.macSize = macSize;
        this.plaintextLimit = plaintextLimit;
        this.cipher = createCipher();
    }

    public byte[] decode(byte[] buf, int off, int len) throws IOException {
        try {
            int encLen = len - macSize;
            byte[] mac = new byte[macSize];
            System.arraycopy(buf, off + encLen, mac, 0, macSize);
            byte[] enc = new byte[encLen];
            System.arraycopy(buf, off, enc, 0, encLen);
            byte[] clear = cipher.doFinal(enc);
            if (!TlsUtils.constantTimeAreEqual(mac, calculateMac(clear))) {
                throw new TlsFatalAlert(AlertDescription.bad_record_mac);
            }
            if (clear.length > plaintextLimit) {
                throw new TlsFatalAlert(AlertDescription.decode_error);
            }
            return clear;
        } catch (GeneralSecurityException e) {
            throw new TlsFatalAlert(AlertDescription.internal_error, e);
        }
    }

    public byte[] calculateMac(byte[] data) {
        return new byte[0];
    }

    private Cipher createCipher() throws IOException {
        try {
            int cipherKeySize = context.getSecurityParameters().getCipherKeySize();
            Cipher cipher = Cipher.getInstance("ChaCha20/CTR/NoPadding");
            byte[] readSecret = getReadSecret();
            byte[] writeSecret = getWriteSecret();
            SecretKeySpec key = new SecretKeySpec(Arrays.copyOf(readSecret, cipherKeySize), "ChaCha20");
            cipher.init(Cipher.DECRYPT_MODE, key, new IvParameterSpec(writeSecret));
            return cipher;
        } catch (GeneralSecurityException e) {
            throw new TlsFatalAlert(AlertDescription.internal_error, e);
        }
    }

    private byte[] getReadSecret() throws IOException {
        if (readSecret == null) {
            readSecret = context.exportSecret(TlsSession.SECRET_READ_MAC);
        }
        return readSecret;
    }

    private byte[] getWriteSecret() throws IOException {
        if (writeSecret == null) {
            writeSecret = context.exportSecret(TlsSession.SECRET_WRITE_MAC);
        }
        return writeSecret;
    }
}
```