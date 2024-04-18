Here's a proposed patch to fix the error:
```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
      throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
      throw new IOException("bad_record_mac");
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

    return output;
  }
```
The `TlsFatalAlert` class has been removed in the new library version, so we replace the `TlsFatalAlert` constructor call with a throwable `IOException` with the same message.