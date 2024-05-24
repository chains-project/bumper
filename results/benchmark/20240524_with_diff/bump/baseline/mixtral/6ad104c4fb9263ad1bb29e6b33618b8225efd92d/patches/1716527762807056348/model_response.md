Here's the fixed `decodeCiphertext` method:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
    throws IOException {

  KeyParameter macKey = initRecordMAC(decryptCipher);

  byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

  if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
    throw new org.bouncycastle.crypto.tls.TlsFatalAlert(new AlertDescription(40));
  }

  byte[] output = new byte[ciphertext.length];
  decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

  return output;
}
```

The changes include importing `AlertDescription` from the new library version and using the constructor `TlsFatalAlert(AlertDescription)` instead of `TlsFatalAlert(short)`.