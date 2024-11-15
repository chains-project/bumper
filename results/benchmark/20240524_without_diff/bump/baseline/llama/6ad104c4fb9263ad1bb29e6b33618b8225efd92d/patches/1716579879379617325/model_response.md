```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    Cipher decryptCipher = Cipher.getInstance("ChaCha20");
    decryptCipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(new byte[32], "ChaCha20"));
    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.equals(calculatedMAC, receivedMAC)) {
        throw new TlsFatalAlert(AlertDescription.bad_record_mac);
    }

    byte[] output = new byte[ciphertext.length];
    decryptCipher.doFinal(ciphertext, 0, ciphertext.length, output, 0);

    return output;
}
```