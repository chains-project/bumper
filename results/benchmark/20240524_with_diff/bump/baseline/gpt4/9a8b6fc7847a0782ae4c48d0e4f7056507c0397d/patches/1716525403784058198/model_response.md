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

        StringDigester digester = new PooledStringDigester();
        digester.setAlgorithm(getAlgorithm());
        digester.setPoolSize(4);
        digester.setSaltSizeBytes(16);
        digester.setStringOutputType("hexadecimal");

        PasswordEncoder encoder = new DigesterPasswordEncoder(digester);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```