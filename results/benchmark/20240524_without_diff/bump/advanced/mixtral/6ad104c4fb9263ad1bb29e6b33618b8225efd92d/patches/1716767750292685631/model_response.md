Here's the fixed `decodeCiphertext` method. I replaced the `org.bouncycastle.crypto.tls.TlsFatalAlert` class with `org.bouncycastle.crypto.TlsFatalAlert`:

```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.TlsFatalAlert(org.bouncycastle.crypto.TlsFatalAlert.bad_record_mac);
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```
This should resolve the error related to the missing `org.bouncycastle.crypto.tls` package.