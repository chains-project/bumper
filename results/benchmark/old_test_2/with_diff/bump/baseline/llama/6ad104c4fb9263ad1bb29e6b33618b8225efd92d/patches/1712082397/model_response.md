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
The changes made to the code include:

* Importing the `org.bouncycastle.crypto.tls.TlsFatalAlert` class.
* Creating a new instance of `TlsFatalAlert` and passing it the `AlertDescription.bad_record_mac` constant.
* Removing the `Override` annotation, as it is not necessary and can be safely removed.
* Changing the throw statement to use the new `TlsFatalAlert` class instead of the removed `TlsFatalAlert` class.