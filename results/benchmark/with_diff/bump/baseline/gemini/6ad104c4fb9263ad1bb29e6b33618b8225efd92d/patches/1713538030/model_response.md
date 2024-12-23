```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder extends TlsBlockCipher {

    private final TlsFatalAlert fatalAlert;

    public ChachaDecoder(TlsCipher cipher, TlsFatalAlert fatalAlert) {
        super(cipher);
        this.fatalAlert = fatalAlert;
    }

    @Override
    public int decode(byte[] input, int inputOff, int len) throws IOException {
        int outputLen = super.decode(input, inputOff, len);
        if (outputLen < 0) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }
        return outputLen;
    }

    @Override
    public int getOutputSize(int inputLen) {
        return super.getOutputSize(inputLen);
    }

    public TlsFatalAlert getFatalAlert() {
        return fatalAlert;
    }
}
```