Here's a proposed patch to fix the error:
```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
      throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
      throw new org.bouncycastle.crypto.tls.TlsFatalAlert(org.bouncycastle.crypto.tls.AlertDescription.bad_record_mac);
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
  }
```
The changes made were:

* `TlsFatalAlert` was replaced with `org.bouncycastle.crypto.tls.TlsFatalAlert`
* `AlertDescription.bad_record_mac` was replaced with `org.bouncycastle.crypto.tls.AlertDescription.bad_record_mac`

These changes are necessary because the `TlsFatalAlert` class and the `AlertDescription` enum have been removed from the updated library version. The replacement classes are from the `org.bouncycastle.crypto.tls` package, which is still available in the updated library version.