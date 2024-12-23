```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public static final int CHACHA_DECODER_ERROR = 0;
    public static final int CHACHA_DECODER_OK = 1;

    private final Cipher cipher;

    public ChachaDecoder(Cipher cipher) {
        this.cipher = cipher;
    }

    public int decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        try {
            cipher.update(in, inOff, len, out, outOff);
            return CHACHA_DECODER_OK;
        } catch (TlsFatalAlert e) {
            if (e.getAlertDescription() == AlertDescription.bad_record_mac) {
                return CHACHA_DECODER_ERROR;
            } else {
                throw e;
            }
        }
    }
}
```