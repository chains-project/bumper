```java
  import org.bouncycastle.crypto.tls.TlsFatalAlert;
  import org.bouncycastle.crypto.tls.TlsSession;
  import org.bouncycastle.crypto.tls.TlsStreamCipher;
  import org.bouncycastle.crypto.tls.TlsUtils;

  import java.io.IOException;
  import java.io.InputStream;
  import java.io.OutputStream;
  import java.security.SecureRandom;

  class ChachaDecoder implements TlsStreamCipher {

      private TlsSession session;
      private SecureRandom random;
      private byte[] key;
      private byte[] iv;
      private byte[] buffer;
      private int pos;

      ChachaDecoder(TlsSession session, SecureRandom random) {
          this.session = session;
          this.random = random;
      }

      public void init(TlsSession session, int readMode) {
          this.session = session;
          this.key = session.getRXChachaKey();
          this.iv = session.getRXChachaIV();
          this.pos = 0;
          this.buffer = new byte[8];
      }

      public byte[] encrypt(byte[] input, int inOff, int len) {
          throw new TlsFatalAlert(AlertDescription.internal_error);
      }

      public byte[] decrypt(byte[] input, int inOff, int len) throws IOException {
          if (len < 16) {
              throw new TlsFatalAlert(AlertDescription.decode_error);
          }

          int plainTextLength = len - 16;
          byte[] output = new byte[plainTextLength];

          int bufPos = pos;
          int posEnd = Math.min(bufPos + (8 - pos), len);

          System.arraycopy(input, inOff, buffer, pos, posEnd - pos);
          pos = posEnd;

          if (pos == 8) {
              byte[] nonce = new byte[12];
              System.arraycopy(iv, 0, nonce, 0, 4);
              System.arraycopy(buffer, 0, nonce, 4, 8);

              int counter = (iv[4] & 0xFF) << 24 | (iv[5] & 0xFF) << 16 | (iv[6] & 0xFF) << 8 | (iv[7] & 0xFF);
              counter++;
              iv[4] = (byte) (counter >> 24);
              iv[5] = (byte) (counter >> 16);
              iv[6] = (byte) (counter >> 8);
              iv[7] = (byte) counter;

              byte[] keyStream = TlsUtils.calculateKeyStream(session.getRXChachaKey(), nonce, 64);

              for (int i = 0; i < plainTextLength; i++) {
                  output[i] = (byte) (input[inOff + 8 + i] ^ keyStream[i]);
              }

              pos = 0;
          }

          return output;
      }

      public void rekey() {
          key = session.getRXChachaKey();
          iv = session.getRXChachaIV();
      }

      public int getPlaintextLimit(int ciphertextLimit) {
          return ciphertextLimit - 16;
      }
  }
```