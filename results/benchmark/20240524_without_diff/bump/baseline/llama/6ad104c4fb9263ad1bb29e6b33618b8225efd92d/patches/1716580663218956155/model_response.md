```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] ciphertext) throws IOException {
    byte[] iv = new byte[16]; // assuming 16 bytes for initialization vector
    return decodeCiphertext(receivedMAC, iv, ciphertext);
}
```