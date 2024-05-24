Here is a possible patch for the code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
    throws IOException {

  KeyParameter macKey = initRecordMAC(decryptCipher);

  byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

  if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
    throw new TlsFatalAlert(new AlertDescription(40));
  }

  byte[] output = new byte[ciphertext.length];
  decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

  return output;
}
```

The change is to replace the usage of `AlertDescription.bad_record_mac` with `new AlertDescription(40)`, which has the same value as `bad_record_mac` (40). This is because the constructor `TlsFatalAlert(short)` has been removed in the new version and it is no longer possible to use `AlertDescription` directly.

It is also a good idea to import the `AlertDescription` class at the beginning of the file to make the code more readable.