Here's the patched method using the added libraries:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.InvalidCipherTextException;
import org.bouncycastle.crypto.StreamCipher;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

import java.io.IOException;

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
        throw new IOException("Error decrypting ciphertext", e);
    }
    return output;
}
```

Changes made:

1. Replaced `TlsFatalAlert` and `AlertDescription` with a custom exception `RuntimeException("bad_record_mac")`.
2. Wrapped `decryptCipher.processBytes` in a try-catch block to handle `DataLengthException` and `InvalidCipherTextException`.
3. Threw an `IOException` with a custom message in case of decryption errors.