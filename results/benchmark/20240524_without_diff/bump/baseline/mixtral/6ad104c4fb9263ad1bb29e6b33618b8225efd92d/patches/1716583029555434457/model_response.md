Here's a proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.StreamCipher;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
        throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new TlsFatalAlert(AlertDescription.bad_record_mac);
    }

    byte[] output = new byte[ciphertext.length];
    try {
        decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    } catch (DataLengthException e) {
        throw new IOException("Failed to decrypt ciphertext", e);
    }

    return output;
}
```

The `DataLengthException` is a new added library method identified with `++`. It's used to catch any exceptions that might occur during the decryption process.