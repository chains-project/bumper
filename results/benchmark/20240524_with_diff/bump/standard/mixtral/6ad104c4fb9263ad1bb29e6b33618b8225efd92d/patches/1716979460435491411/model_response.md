Here's the fixed version of the `decodeCiphertext` method that takes into account the changes in the new library version:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(7)); // Use AlertDescription with a specific value
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```

In the new library version, the constructor for `TlsFatalAlert` has been removed, and `getAlertDescription()` is not available anymore. To fix the issue, you can replace the constructor call with a new `AlertDescription` instance and pass the specific value for the error code (7 in this case).