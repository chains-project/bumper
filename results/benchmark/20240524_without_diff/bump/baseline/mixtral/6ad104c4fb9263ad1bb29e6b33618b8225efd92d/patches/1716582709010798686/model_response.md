Here's a proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.StreamCipher;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
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

I added a try-catch block to handle the `DataLengthException` that can be thrown by the `processBytes` method of the `StreamCipher` class. This exception can occur if the length of the input data is not a multiple of the block size of the cipher. By catching this exception and wrapping it in an `IOException`, the code can handle this error gracefully.

Note that I assumed that the `decryptCipher` variable is an instance of `StreamCipher`. If this is not the case, please provide more context about the type of `decryptCipher` so that I can adjust the patch accordingly.