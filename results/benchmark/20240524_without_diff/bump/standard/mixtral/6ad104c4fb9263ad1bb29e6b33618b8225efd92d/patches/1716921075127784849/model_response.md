Here's a possible patch for the code to fix the error:

```java
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.ByteBuffer;
import java.security.GeneralSecurityException;
import java.util.Arrays;

public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws GeneralSecurityException {
    SecretKeySpec macKey = initRecordMAC(decryptCipher);
    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);
    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new RuntimeException("Bad MAC");
    }
    byte[] iv = Arrays.copyOfRange(ciphertext, 0, 12);
    byte[] encryptedData = Arrays.copyOfRange(ciphertext, 12, ciphertext.length);
    IvParameterSpec ivParamSpec = new IvParameterSpec(iv);
    Cipher cipher = Cipher.getInstance("ChaCha20-Poly1305");
    cipher.init(Cipher.DECRYPT_MODE, macKey, ivParamSpec);
    byte[] output = cipher.doFinal(encryptedData);
    return output;
}
```

Note that this patch uses the `javax.crypto` package instead of `org.bouncycastle.crypto` for encryption and decryption. It also defines a new `PolyKeyCreator` class to generate the MAC key. You may need to implement this class yourself based on the original `PolyKeyCreator` class from the `io.github.hapjava.server.impl.crypto` package.

Also, the `decryptCipher` variable is not defined in the provided code snippet, so I assumed it's an instance variable of the enclosing class. If it's not the case, you may need to adjust the code accordingly.

Finally, the patch throws a `RuntimeException` instead of `org.bouncycastle.crypto.tls.TlsFatalAlert` when the MAC check fails. You may want to define your own exception class for this purpose.