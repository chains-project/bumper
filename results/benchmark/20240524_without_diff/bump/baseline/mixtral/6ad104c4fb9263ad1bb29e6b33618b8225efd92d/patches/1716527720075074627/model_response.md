Here's the proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
    throws IOException {

  KeyParameter macKey = initRecordMAC(decryptCipher);

  byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

  if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
    throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(7));
  }

  byte[] output = new byte[ciphertext.length];
  decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

  return output;
}
```

The changes made include:

1. Importing `AlertDescription` from the correct package.
2. Creating a new `AlertDescription` instance with the value of `7` (which corresponds to `bad_record_mac`).
3. Creating a new `TlsFatalAlert` instance using the newly created `AlertDescription`.

This patch should resolve the error caused by the missing `AlertDescription` class.