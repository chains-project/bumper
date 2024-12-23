Here's the patched method with the error fixed:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
    throws IOException {

  KeyParameter macKey = initRecordMAC(decryptCipher);

  byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

  if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
    throw new TlsFatalAlert(new TlsFatalAlert(AlertDescription.bad_record_mac));
  }

  byte[] output = new byte[ciphertext.length];
  decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

  return output;
}
```

The change includes importing the `TlsFatalAlert` class, and wrapping the `AlertDescription.bad_record_mac` in a new `TlsFatalAlert` constructor.