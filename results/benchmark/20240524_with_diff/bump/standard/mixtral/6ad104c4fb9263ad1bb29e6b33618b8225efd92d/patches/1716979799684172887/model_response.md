Here's the fixed `decodeCiphertext` method using the new library version:

```java
import org.bouncycastle.crypto.DataLengthException;
import org.bouncycastle.crypto.InvalidCipherTextException;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
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

The `TlsFatalAlert` and `AlertDescription` classes have been removed, so I replaced the exception with a `RuntimeException` and custom message for the MAC validation. Additionally, I wrapped the `processBytes` call in a try-catch block to handle the new exceptions introduced in the new library version.