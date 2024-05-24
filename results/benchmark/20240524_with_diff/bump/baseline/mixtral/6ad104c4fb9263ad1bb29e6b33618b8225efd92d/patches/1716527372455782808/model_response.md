Here's the proposed patch for the `decodeCiphertext` method:

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

The change includes importing the `AlertDescription` class from the `org.bouncycastle.crypto.tls` package and modifying the `TlsFatalAlert` constructor call to accept an `AlertDescription` instance instead of a short value. The `AlertDescription` instance is constructed with the value `40`, which corresponds to the `bad_record_mac` value.