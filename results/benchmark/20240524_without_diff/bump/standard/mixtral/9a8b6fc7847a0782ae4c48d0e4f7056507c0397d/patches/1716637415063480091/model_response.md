Here's the proposed patch:

```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.util.password.StrongPasswordEncryptor encryptor = new org.jasypt.util.password.StrongPasswordEncryptor();
        String encryptedPassword = encryptor.encryptPassword(new String(chars));
        return new BCryptPasswordEncoder().encode(encryptedPassword);
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

Instead of using `org.jasypt.spring.security.PBEPasswordEncoder`, I used `org.jasypt.util.password.StrongPasswordEncryptor` and `org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder` to encrypt the password.

Note that this solution assumes that the `getAlgorithm()` method returns a value that's compatible with `BCryptPasswordEncoder`. If not, you may need to modify the algorithm or use a different password encoder.