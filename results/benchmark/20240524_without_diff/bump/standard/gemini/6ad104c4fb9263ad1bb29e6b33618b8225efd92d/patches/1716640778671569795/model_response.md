```java
import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.ByteToMessageDecoder;
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsUtils;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.List;

public class ChachaDecoder extends ByteToMessageDecoder {

    private static final int IV_LENGTH = 12;
    private static final int MAC_LENGTH = 16;

    private final TlsContext context;
    private final TlsCipher cipher;

    public ChachaDecoder(TlsContext context, TlsCipher cipher) {
        this.context = context;
        this.cipher = cipher;
    }

    @Override
    protected void decode(ChannelHandlerContext ctx, ByteBuf in, List<Object> out) throws Exception {
        if (in.readableBytes() < IV_LENGTH) {
            return;
        }

        byte[] iv = new byte[IV_LENGTH];
        in.readBytes(iv);

        byte[] encryptedData = new byte[in.readableBytes() - MAC_LENGTH];
        in.readBytes(encryptedData);

        byte[] mac = new byte[MAC_LENGTH];
        in.readBytes(mac);

        byte[] plaintext;
        try {
            plaintext = cipher.decrypt(iv, encryptedData, 0, encryptedData.length);
        } catch (IOException e) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac, e);
        }

        if (!TlsUtils.verifyMac(context, MAC_LENGTH, mac, 0, plaintext, 0)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        out.add(new ByteBuffer(plaintext));
    }
}
```