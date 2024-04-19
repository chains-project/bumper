```java
import org.bouncycastle.crypto.tls.AlertLevel;

import org.bouncycastle.crypto.tls.TlsFatalAlert;

  import org.bouncycastle.crypto.tls.TlsProtocol;

  import org.bouncycastle.crypto.tls.TlsUtils;

  

  /**

   * A ChaCha20Poly1305 cipher, for use with TLS 1.3.

   */

  public class ChachaDecoder extends AbstractTlsCipher

  {

      protected TlsContext context;

      protected TlsMac mac;

      protected byte[] secret;

      protected int nonce_explicit;



      /**

       * Constructor for a ChaCha20Poly1305 cipher.

       *

       * @param context   the TLS context

       * @param isRead    whether this is the read or write cipher

       */

      public ChachaDecoder(TlsContext context, boolean isRead)

      {

          super(context, isRead);



          this.context = context;

          this.mac = new TlsMac(new Poly1305(), TlsUtils.PRF_SHA256, context.getSecurityParameters().getPrfAlgorithm(), 16, null, 0);

          this.secret = TlsUtils.PRF(context, context.getSecurityParameters().getPrfAlgorithm(), null, null, 32);

          this.nonce_explicit = isRead ? 1 : 0;

      }



      protected TlsCipher buildCipher(TlsContext context, int cipherType, byte[] key, byte[] iv)

      {

          return new Chacha20Cipher(key, iv);

      }



      protected byte[] calculateKeyBlock(int length)

      {

          return TlsUtils.calculateKeyBlock(context, secret, length);

      }



      protected int getCiphertextDecodeLimit(int plaintextLimit)

      {

          return plaintextLimit + mac.getSize();

      }



      protected int getCiphertextEncodeLimit(int plaintextLength, int extra)

      {

          return plaintextLength + extra + mac.getSize();

      }



      protected void rekeyCipher()

      {

          TlsMac newMac = new TlsMac(new Poly1305(), TlsUtils.PRF_SHA256, context.getSecurityParameters().getPrfAlgorithm(), 16, null, 0);

          newMac.setKey(calculateKeyBlock(mac.getSize()));



          if (isRead)

          {

              mac = newMac;

          }

          else

          {

              byte[] oldSecret = secret;

              secret = new byte[oldSecret.length];

              System.arraycopy(oldSecret, 0, secret, 0, oldSecret.length);

              TlsUtils.writeUint64(context.getNonceRandom(), secret, 8);

              TlsUtils.writeUint32(context.getNonceRandom(), secret, 16);

              mac = newMac;

          }

      }



      protected byte[] decodeCiphertext(int seqNo, byte[] input, int inOff, int len)

      {

          int encLen = len - mac.getSize();

          byte[] output = new byte[encLen];

          cipher.decrypt(input, inOff, encLen, output, 0);



          // TODO Need to check the length of the explicit nonce, if it's there.

          int macInputLen = encLen + nonce_explicit;

          byte[] macInput = new byte[macInputLen];

          System.arraycopy(input, inOff, macInput, 0, macInputLen);

          byte[] macResult = mac.calculateMac(seqNo, macInput, 0, macInputLen);



          if (!TlsUtils.constantTimeAreEqual(macResult, 0, input, inOff + encLen, mac.getSize()))

          {

              throw new TlsFatalAlert(AlertDescription.bad_record_mac, "ChaCha20Poly1305 bad MAC");

          }



          return output;

      }



      protected byte[] encodePlaintext(int seqNo, byte[] input, int inOff, int len)

      {

          byte[] output = new byte[len + mac.getSize()];

          cipher.encrypt(input, inOff, len, output, 0);



          // TODO Need to check the length of the explicit nonce, if it's there.

          int macInputLen = len + nonce_explicit;

          byte[] macInput = new byte[macInputLen];

          System.arraycopy(output, 0, macInput, 0, macInputLen);

          byte[] macResult = mac.calculateMac(seqNo, macInput, 0, macInputLen);

          System.arraycopy(macResult, 0, output, len, mac.getSize());



          return output;

      }

  }
```