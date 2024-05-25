```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] ciphertext) throws IOException {
    byte[] iv = new byte[12]; // assuming the second parameter is an initialization vector
    return decodeCiphertext(receivedMAC, iv, ciphertext);
}
```