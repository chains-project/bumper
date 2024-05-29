Here's a proposed patch for the `decodeCiphertext` method that removes the usage of the `AlertDescription` class, which seems to be causing the error:

```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(80); // bad_record_mac is 80
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```

This patch replaces the usage of `org.bouncycastle.crypto.tls.AlertDescription.bad_record_mac` with a hardcoded value of `80`, which is the actual value of the `bad_record_mac` constant. This should resolve the "cannot find symbol" error.