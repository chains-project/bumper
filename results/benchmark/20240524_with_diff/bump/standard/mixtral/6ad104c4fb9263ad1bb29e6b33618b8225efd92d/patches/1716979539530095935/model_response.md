Here's the proposed patch:

```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new org.bouncycastle.crypto.tls.AlertDescription(80), "bad_record_mac");
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```

In the new version of the library, the constructor for `TlsFatalAlert` has been removed, and a new method `getAlertDescription()` has been added. To fix the error, we can create a new `AlertDescription` object with the appropriate value (80 for `bad_record_mac`), and pass it to the `TlsFatalAlert` constructor.