Here's the patched `decodeCiphertext` method using the new library version:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(7));
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```

The changes include:

* Importing the `AlertDescription` class from the `org.bouncycastle.crypto.tls` package.
* Creating a new `AlertDescription` instance with the value `7` (bad\_record\_mac) when throwing a `TlsFatalAlert`.

These changes should resolve the "cannot find symbol" error related to `AlertDescription`.