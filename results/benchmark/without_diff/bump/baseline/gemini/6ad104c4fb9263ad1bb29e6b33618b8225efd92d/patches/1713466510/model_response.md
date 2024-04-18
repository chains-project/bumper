```java
  import org.bouncycastle.crypto.tls.TlsCipher;

  import javax.crypto.Cipher;
  import javax.crypto.spec.IvParameterSpec;
  import javax.crypto.spec.SecretKeySpec;
  import java.io.IOException;
  import java.security.GeneralSecurityException;
  import java.security.SecureRandom;
  import java.util.Arrays;

  public class ChachaDecoder {

      private static final int MAC_SIZE = 16;

      private final TlsCipher cipher;
      private final byte[] additionalData;
      private final SecureRandom random;

      public ChachaDecoder(TlsCipher cipher, byte[] additionalData, SecureRandom random) {
          this.cipher = cipher;
          this.additionalData = additionalData;
          this.random = random;
      }

      public byte[] decode(byte[] buf, int off, int len) throws IOException {
          if (len < MAC_SIZE) {
              throw new TlsFatalAlert(AlertDescription.decode_error);
          }

          byte[] mac = Arrays.copyOfRange(buf, off + len - MAC_SIZE, off + len);
          len -= MAC_SIZE;

          // 2.2. Generate a random value (nonce)
          byte[] nonce = new byte[12];
          random.nextBytes(nonce);

          // 2.3. Compute additionalData = seq_num + random
          byte[] ad = new byte[12 + additionalData.length];
          System.arraycopy(nonce, 0, ad, 0, 12);
          System.arraycopy(additionalData, 0, ad, 12, additionalData.length);

          // 2.4. Encrypt content using the AEAD cipher with nonce and additionalData
          try {
              cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(cipher.getKey(), "ChaCha20"), new IvParameterSpec(nonce));
              byte[] content = cipher.doFinal(buf, off, len, ad, 0, ad.length);

              // 2.5. Verify the MAC
              if (!Arrays.equals(mac, cipher.doFinal(new byte[0]))) {
                  throw new TlsFatalAlert(AlertDescription.bad_record_mac);
              }

              return content;
          } catch (GeneralSecurityException e) {
              throw new TlsFatalAlert(AlertDescription.internal_error, e);
          }
      }
  }
```