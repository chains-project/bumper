Here's the fixed `createStringEncoder` method:

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

        TextEncryptor encryptor = new org.jasypt.util.text.StrongTextEncryptor();
        encryptor.setPasswordCharArray(chars);

        return new org.jasypt.spring.security.PasswordEncoder() {
            @Override
            public String encodePassword(String rawPass, Object salt) {
                return encryptor.encrypt(rawPass);
            }

            @Override
            public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
                return encPass.equals(encryptor.encrypt(rawPass));
            }
        };
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

This version of the method now uses the added `TextEncryptor` from the library to encrypt and validate passwords. It creates an anonymous class implementing the `PasswordEncoder` interface for compatibility with the original method signature.