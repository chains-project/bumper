```java
private byte[] decrypt(byte[] msg) {
    byte[] mac = new byte[16];
    byte[] ciphertext = new byte[msg.length - 16];
    System.arraycopy(msg, 0, ciphertext, 0, msg.length - 16);
    System.arraycopy(msg, msg.length - 16, mac, 0, 16);
    byte[] additionalData =
        ByteBuffer.allocate(2)
            .order(ByteOrder.LITTLE_ENDIAN)
            .putShort((short) (msg.length - 16))
            .array();
    try {
      byte[] nonce = Pack.longToLittleEndian(inboundBinaryMessageCount++);
      ChachaDecoder decoder = new ChachaDecoder(readKey, nonce);
      return decoder.decodeCiphertext(mac, additionalData, ciphertext, ciphertext.length);
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
}
```