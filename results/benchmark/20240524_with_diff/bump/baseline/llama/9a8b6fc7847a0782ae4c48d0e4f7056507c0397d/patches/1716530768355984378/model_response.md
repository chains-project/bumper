```java
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        StringEncryptor stringEncryptor = new StandardPBEStringEncryptor();
        stringEncryptor.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncryptor.setProviderName(getProviderName());
        }
        stringEncryptor.setAlgorithm(getAlgorithm());

        PasswordEncryptor passwordEncryptor = new StandardPBEStringEncryptor();
        passwordEncryptor.setStringEncryptor(stringEncryptor);

        PasswordEncoder encoder = new PasswordEncoder();
        encoder.setPasswordEncryptor(passwordEncryptor);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```