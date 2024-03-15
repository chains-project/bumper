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

        org.springframework.security.crypto.password.Pbkdf2PasswordEncoder encoder = new org.springframework.security.crypto.password.Pbkdf2PasswordEncoder(new String(chars));

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```
In the code above, I replaced the `PBEPasswordEncoder` with `Pbkdf2PasswordEncoder` from the Spring Security Crypto library, as the former was removed from the new library version. This encoder is a password encoder that uses the PBKDF2 hashing function. I also removed the line where we set the `PBEStringEncryptor` as it's not applicable to the new encoder.