Here is a fixed version of the `decodeCiphertext` method that should resolve the error:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
    throws IOException {

  KeyParameter macKey = initRecordMAC(decryptCipher);

  byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

  if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
    throw new TlsFatalAlert(new AlertDescription(40)); // 40 corresponds to bad_record_mac
  }

  byte[] output = new byte[ciphertext.length];
  decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

  return output;
}
```

The only change made is to replace the `TlsFatalAlert` constructor with a new one that takes an `AlertDescription` parameter. Since the `AlertDescription` enum has not been removed, we can still use it to create an `AlertDescription` instance. The `AlertDescription` instance is then used to construct a new `TlsFatalAlert`.

Note that the `AlertDescription` enum is still present in the new library version, so there should be no issues with using it.