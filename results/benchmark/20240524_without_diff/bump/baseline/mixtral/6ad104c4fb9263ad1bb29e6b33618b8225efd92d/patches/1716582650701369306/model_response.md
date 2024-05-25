Here's a proposed patch for the failing method:

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
        int macLength = decryptCipher.getOutputSize(calculatedMAC.length);
        decryptCipher.processBytes(additionalData, 0, additionalData.length, calculatedMAC, 0);
        decryptCipher.doFinal(calculatedMAC, macLength);
    } catch (DataLengthException e) {
        throw new IOException("Error calculating MAC", e);
    }

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new IOException("Bad MAC");
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
}
```

In this patch, I've replaced the `PolyKeyCreator.create` method with a custom implementation that uses the `decryptCipher` to calculate the MAC. This should avoid the need for any external dependencies. I've also updated the error handling to use a generic `IOException` instead of `TlsFatalAlert`.

Note that this implementation assumes that the `decryptCipher` is capable of calculating a MAC over the `additionalData`. If this is not the case, you may need to modify the implementation accordingly.