Here's the patched method using the added library methods:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.InvalidCipherTextException;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;
import java.nio.ByteBuffer;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new RuntimeException("bad_record_mac");
    }
    byte[] output = new byte[ciphertext.length];
    try {
        decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    } catch (DataLengthException | InvalidCipherTextException e) {
        throw new IOException("Failed to decrypt ciphertext", e);
    }
    return output;
}
```

In this patched method, I replaced the removed `TlsFatalAlert` class with a `RuntimeException` with the error message "bad_record_mac". Also, I replaced the removed `AlertDescription` class with a custom error message. I wrapped the `processBytes` method call in a try-catch block to handle `DataLengthException` and `InvalidCipherTextException` and re-throw them as an `IOException`.