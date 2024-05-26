Here is the updated `decodeCiphertext` method with the error fixed:

```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws java.io.IOException {
    org.bouncycastle.crypto.params.KeyParameter macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = io.github.hapjava.server.impl.crypto.PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!org.bouncycastle.util.Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new org.bouncycastle.crypto.tls.AlertDescription(10));
    }

    byte[] output = new byte[ciphertext.length];
    int processed = decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output,  typo fixed here 0);
    if (processed != ciphertext.length) {
        throw new IOException("Failed to decrypt ciphertext");
   
    }

    return output;
}
``
```