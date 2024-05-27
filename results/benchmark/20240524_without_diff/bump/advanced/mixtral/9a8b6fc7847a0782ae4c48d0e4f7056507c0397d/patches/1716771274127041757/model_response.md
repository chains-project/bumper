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
        return new org.acegisecurity.providers.encoding.ShaPasswordEncoder(256).encodePassword(encryptedPassword, null);
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

I replaced the `org.jasypt.spring.security.PBEPasswordEncoder` class with `org.acegisecurity.providers.encoding.ShaPasswordEncoder` and `org.jasypt.util.password.StrongPasswordEncryptor` to avoid using the removed library method `setPbeStringEncryptor`. The `ShaPasswordEncoder` class uses the SHA-256 algorithm by default, so I added a new instance of `StrongPasswordEncryptor` to encrypt the password using a strong algorithm before encoding it with `ShaPasswordEncoder`.