Here's the proposed patch for the given client code:

```java
@java.lang.Override
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
        org.jasypt.util.text.TextEncryptor encryptor = new org.jasypt.util.text.TextEncryptor();
        encryptor.setPbeStringEncryptor(stringEncrypter);
        org.jasypt.spring.security.PasswordEncoder passwordEncoder = new org.jasypt.spring.security.PasswordEncoder();
        passwordEncoder.setEncryptor(encryptor);
        return passwordEncoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The changes made are:

* Imported `org.jasypt.util.text.TextEncryptor` to replace the removed `org.jasypt.spring.security.PBEPasswordEncoder`.
* Created a new instance of `TextEncryptor` and set the `PBEStringEncryptor` to it.
* Created a new instance of `PasswordEncoder` and set the `Encryptor` to the `TextEncryptor` instance.

This patch should fix the error caused by the missing `PBEPasswordEncoder` constructor.