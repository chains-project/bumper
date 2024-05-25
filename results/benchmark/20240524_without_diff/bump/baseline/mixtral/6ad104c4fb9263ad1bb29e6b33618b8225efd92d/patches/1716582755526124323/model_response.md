Here's a proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;
import java.security.SecureRandom;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
        throws IOException {

    SecureRandom random = new SecureRandom();
    byte[] macKey = new byte[32];
    random.nextBytes(macKey);

    KeyParameter macKeyParameter = new KeyParameter(macKey);

    byte[] calculatedMAC = PolyKeyCreator.create(macKeyParameter, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new TlsFatalAlert(AlertDescription.bad_record_mac);
    }

    byte[] output = new byte[ciphertext.length];
    try {
        decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    } catch (DataLengthException e) {
        throw new IOException("Error processing ciphertext", e);
    }

    return output;
}
```

In this patch, I've replaced the `initRecordMAC` method with a new way of generating a random `KeyParameter` for the MAC key. This should resolve the "cannot find symbol" error. Note that this is just one possible way to generate a random MAC key, and you may want to modify this code to fit your specific use case.