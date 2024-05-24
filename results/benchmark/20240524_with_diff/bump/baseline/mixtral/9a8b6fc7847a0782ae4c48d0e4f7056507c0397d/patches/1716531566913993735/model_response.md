Here's the fixed `createStringEncoder` method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        StringEncryptor stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());

        TextEncryptor textEncryptor = new org.jasypt.encryption.pbe.PBETextEncryptor();
        textEncryptor.setPasswordCharArray(chars);
        textEncryptor.setStringEncryptor(stringEncrypter);

        return new org.jasypt.spring.security.PasswordEncoder() {
            @Override
            public String encodePassword(String rawPass, Object salt) {
                return textEncryptor.encrypt(rawPass);
            }

            @Override
            public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
                return encPass.equals(textEncryptor.encrypt(rawPass));
            }
        };
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

This solution creates a custom `PasswordEncoder` implementation that wraps the provided `TextEncryptor`. This allows the use of the new library methods `TextEncryptor` and `PasswordEncoder` while maintaining the method signature and functionality.