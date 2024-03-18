```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());

        PBEPasswordEncoder encoder = new PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);

        return encoder;
    } finally {
        Arrays.fill(password, (byte) 0);
        Arrays.fill(chars, (char) 0);
    }
}
```
Here, the `scramble` method seems to be missing in the current library. Hence, I have replaced it with `Arrays.fill` method which is a standard Java method to fill an array with a specific value. This will ensure that the `password` and `chars` arrays are filled with zero, effectively scrambling the data.