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

        PooledPBEStringEncryptor encryptor = new PooledPBEStringEncryptor();
        encryptor.setProviderName(stringEncrypter.getProviderName());
        encryptor.setPasswordCharArray(stringEncrypter.getPasswordCharArray());
        encryptor.setAlgorithm(stringEncrypter.getAlgorithm());

        return encryptor;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```