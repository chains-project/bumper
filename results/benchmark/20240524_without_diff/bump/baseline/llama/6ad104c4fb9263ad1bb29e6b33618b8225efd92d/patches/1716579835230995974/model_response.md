```java
public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext) throws IOException {
    KeyParameter macKey = initRecordMAC(decryptCipher);
    CipherParameters params = new ParametersWithIV(macKey, new byte[PolyKeyCreator.IV_LENGTH]);
    BlockCipher cipher = new CBCBlockCipher(new AEADBlockCipher(new ChaChaEngine()));
    cipher.init(false, params);
    byte[] calculatedMAC = new byte[cipher.getMac().getMacSize()];
    cipher.processBytes(additionalData, 0, additionalData.length, calculatedMAC, 0);
    cipher.processBytes(ciphertext, 0, ciphertext.length, calculatedMAC, additionalData.length);
    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
        throw new TlsFatalAlert(AlertDescription.bad_record_mac);
    }
    byte[] output = new byte[ciphertext.length];
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length, output, 0);
    return output;
}
```