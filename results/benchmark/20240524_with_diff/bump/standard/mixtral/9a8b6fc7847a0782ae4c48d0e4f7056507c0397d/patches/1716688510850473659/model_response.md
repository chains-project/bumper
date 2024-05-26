Here's the fixed method with the necessary changes to adapt to the new library version:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.util.text.TextEncryptor encryptor = new org.jasypt.util.text.TextEncryptor();
        encryptor.setPbeStringEncryptor(stringEncrypter);
        PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPasswordEncryptor(encryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The main changes are:

1. Replace `org.jasypt.spring.security.PBEPasswordEncoder` with `org.jasypt.spring.security.PasswordEncoder`.
2. Replace `org.jasypt.spring.security.PBEPasswordEncoder` constructor with `org.jasypt.spring.security.PasswordEncoder` constructor.
3. Replace `setPbeStringEncryptor` with `setPasswordEncryptor` and use `org.jasypt.util.text.TextEncryptor` instead of `org.jasypt.encryption.pbe.PBEStringEncryptor`.