Here's a proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.StreamCipher;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = new byte[receivedMAC.length];
    try {
        decryptCipher.processBytes(additionalData, 0, additionalData.length, calculatedMAC, 0);
        decryptCipher.processBytes(ciphertext, 0, ciphertext.length, calculatedMAC, additionalData.length);
    } catch (DataLengthException e) {
        throw new IOException("Error processing ciphertext", e);
    }

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new IOException("Bad record MAC");
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
}
```

The changes I made include:

* Importing the `DataLengthException` class from the `org.bouncycastle.crypto` package.
* Replacing the call to `PolyKeyCreator.create()` with a manual calculation of the MAC using the `decryptCipher`.
* Wrapping the `decryptCipher.processBytes()` calls in a try-catch block to handle `DataLengthException`.
* Replacing the `TlsFatalAlert` exception with a custom `IOException`.
* Replacing the `AlertDescription.bad_record_mac` constant with a custom error message.

Note that these changes are based on the assumption that the `decryptCipher` object is an instance of `StreamCipher` from the `org.bouncycastle.crypto` package. If this assumption is incorrect, then the patch may not work as intended.