Here is a proposed patch for the failing client code:
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
        throw new IOException("Error decrypting ciphertext", e);
    }

    return output;
}
```
In this patch, I added a try-catch block around the call to `decryptCipher.processBytes()` to handle the `DataLengthException` that might be thrown if the length of the input data is not a multiple of the block size of the cipher. I also added an `import` statement for the `DataLengthException` class.

Note: I assumed that the `decryptCipher` variable is an instance of `StreamCipher` class from Bouncy Castle library. If this is not the case, the solution might be different.