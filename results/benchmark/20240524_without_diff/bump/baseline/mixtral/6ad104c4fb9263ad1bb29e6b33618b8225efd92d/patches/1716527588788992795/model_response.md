Here is a possible patch for the code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
    throws IOException {

  KeyParameter macKey = initRecordMAC(decryptCipher);

  byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

  if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
    throw new RuntimeException("Bad MAC");
  }

  byte[] output = new byte[ciphertext.length];
  decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);

  return output;
}
```

This patch removes the `TlsFatalAlert` class, which is no longer available in the updated library, and replaces it with a `RuntimeException`. The `AlertDescription` class is still used, but it has not been removed from the library.

Note that this patch may not be the best solution for your specific use case. It is always a good idea to thoroughly test any changes to your code to ensure that it still behaves as expected.