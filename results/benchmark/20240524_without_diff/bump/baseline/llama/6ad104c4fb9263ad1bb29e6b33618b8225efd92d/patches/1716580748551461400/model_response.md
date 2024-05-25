```
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] ciphertext) throws IOException {
    byte[] iv = new byte[12];
    return decodeCiphertext(receivedMAC, iv, ciphertext);
}
```