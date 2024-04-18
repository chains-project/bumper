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

* Changing `TlsFatalAlert` to `org.bouncycastle.crypto.tls.TlsFatalAlert` to use the updated class name.
* Changing `AlertDescription.bad_record_mac` to `org.bouncycastle.crypto.tls.AlertDescription.bad_record_mac` to use the updated constant.

With these changes, the code should now compile and run without any errors related to the `TlsFatalAlert` class.