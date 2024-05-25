Here's a possible patch for the failing client code:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.StreamCipher;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
        throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = new byte[receivedMAC.length];
    try {
        decryptCipher.processBytes(additionalData, 0, additionalData.length, calculatedMAC, 0);
        decryptCipher.processBytes(ciphertext, 0, ciphertext.length, calculatedMAC, additionalData.length);
    } catch (DataLengthException e) {
        throw new IOException("Error processing ciphertext", e);
    }

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new TlsFatalAlert(AlertDescription.bad_record_mac);
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
}
```

The patch removes the call to `PolyKeyCreator.create()`, which seems to be causing the compilation error. Instead, it calculates the MAC by processing both the `additionalData` and `ciphertext` through the `decryptCipher` stream cipher. This assumes that the `decryptCipher` has been properly initialized to use the same key and nonce as the original MAC calculation. If this is not the case, the patch may need to be modified accordingly.

Note that the patch uses the `DataLengthException` class from the Bouncy Castle library to handle the case where the input data length exceeds the maximum allowed by the stream cipher. This exception is thrown by the `processBytes()` method of the `StreamCipher` interface, which is implemented by the `decryptCipher` object. The patch catches this exception and wraps it in an `IOException` to be consistent with the original method signature. If the `DataLengthException` is not thrown, the patch proceeds with the rest of the MAC comparison and decryption as before.