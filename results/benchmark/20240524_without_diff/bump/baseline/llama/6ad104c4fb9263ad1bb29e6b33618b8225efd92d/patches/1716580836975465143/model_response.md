```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] ciphertext) throws IOException {
    byte[] iv = new byte[12]; // assuming 12 bytes for initialization vector
    return decodeCiphertext(receivedMAC, iv, ciphertext);
}
```