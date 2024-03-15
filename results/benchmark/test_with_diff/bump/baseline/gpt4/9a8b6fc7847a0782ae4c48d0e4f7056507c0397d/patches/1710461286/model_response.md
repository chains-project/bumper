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

        // Create a new PasswordEncoder using the new library
        PasswordEncoder encoder = new PasswordEncoder();
        encoder.setPasswordEncryptor(stringEncrypter);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```
In the updated code, I have replaced PBEPasswordEncoder with PasswordEncoder as PBEPasswordEncoder is removed from the new library. Also, I have replaced `setPbeStringEncryptor` with `setPasswordEncryptor` as the former is not available in the new library.