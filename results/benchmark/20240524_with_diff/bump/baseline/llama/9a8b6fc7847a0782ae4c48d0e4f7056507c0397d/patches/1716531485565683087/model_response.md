```java
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        PasswordEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            encryptor.setProviderName(getProviderName());
        }
        encryptor.setAlgorithm(getAlgorithm());

        PasswordEncoder encoder = new PasswordEncoder();
        encoder.setPasswordEncryptor(encryptor);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```