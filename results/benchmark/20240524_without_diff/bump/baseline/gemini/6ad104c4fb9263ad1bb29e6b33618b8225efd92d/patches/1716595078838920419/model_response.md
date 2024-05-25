```java
  public byte[] decodeCiphertext(byte[] receivedMAC, byte[] additionalData, byte[] ciphertext)
      throws IOException {

    KeyParameter macKey = initRecordMAC(decryptCipher);

    byte[] calculatedMAC = PolyKeyCreator.create(macKey, additionalData, ciphertext);

    if (!Arrays.constantTimeAreEqual(calculatedMAC, receivedMAC)) {
      throw new TlsFatalAlert(AlertDescription.bad_record_mac);
    }

    // Calculate the padding length from the last byte
    int paddingLength = ciphertext[ciphertext.length - 1] & 0xFF;

    // Validate that the padding length is within the valid range
    if (paddingLength > ciphertext.length || paddingLength < 1) {
      throw new TlsFatalAlert(AlertDescription.decryption_failed);
    }

    // Create a new byte array to store the plaintext
    byte[] plaintext = new byte[ciphertext.length - paddingLength];

    // Decrypt the ciphertext and remove the padding
    decryptCipher.processBytes(ciphertext, 0, ciphertext.length - paddingLength, plaintext, 0);

    return plaintext;
  }
```