```java
import develop.p2p.lib.*;
import develop.p2p.lib.P2PPacket;

public class NPCTeleport {

    public void onEnable() {
        P2PPacket p2pPacket = new P2PPacket(1);
        p2pPacket.writeBoolean(true);
        p2pPacket.writeFloat(1.0f);
        p2pPacket.writeDouble(1.0d);
        p2pPacket.writeInt(1);
        p2pPacket.writeLong(1L);
        p2pPacket.writeString("Hello, world!");
        p2pPacket.writeShort((short) 1);
        p2pPacket.writeByte((byte) 1);
        p2pPacket.writeByteArray(new byte[]{1, 2, 3});
        p2pPacket.writeCharArray(new char[]{'a', 'b', 'c'});
        p2pPacket.writeDoubleArray(new double[]{1.0, 2.0, 3.0});
        p2pPacket.writeFloatArray(new float[]{1.0f, 2.0f, 3.0f});
        p2pPacket.writeIntArray(new int[]{1, 2, 3});
        p2pPacket.writeLongArray(new long[]{1L, 2L, 3L});
        p2pPacket.writeObject("Hello, world!");
        p2pPacket.send();
    }
}
```