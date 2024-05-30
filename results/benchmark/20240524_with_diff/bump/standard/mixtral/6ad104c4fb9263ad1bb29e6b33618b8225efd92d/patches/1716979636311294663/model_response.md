Here's a fixed version of the method that adapts to the new library version:

```java
import java.io.IOException;
import java.util.Objects;

import org.bouncycastle.crypto.CipherParameters;
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.util.Arrays;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    CipherParameters macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new RuntimeException("bad_record_mac");
    }
    byte[] output = new byte[ciphertext.length];
    try {
        decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    } catch (DataLengthException e) {
        throw new IOException("Failed to decrypt ciphertext", e);
    }
    return output;
}

private CipherParameters initRecordMAC(CipherParameters decryptCipher) {
    // Implement the logic to initialize the macKey using decryptCipher
    // ...
}

static class PolyKeyCreator {
    static byte[] create(CipherParameters macKey, byte[] additionalData, byte[] ciphertext) {
        // Implement the logic to create calculatedMAC using macKey, additionalData and ciphertext
        // ...
    }
}
```

This new version removes the dependency on the `org.bouncycastle.crypto.tls` package, and instead of throwing a `TlsFatalAlert`, it throws a `RuntimeException` with the message "bad_record_mac". Also, the `DataLengthException` is caught and re-thrown as an `IOException`.