Here is the patched code:
```java
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

        PasswordEncoder encoder = new PasswordEncoder();
        encoder.setPasswordEncryptor(stringEncrypter);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```