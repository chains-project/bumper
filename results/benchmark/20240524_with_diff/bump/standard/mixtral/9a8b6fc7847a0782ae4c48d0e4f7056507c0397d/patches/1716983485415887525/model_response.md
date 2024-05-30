Here is a possible patch for the failing client code:
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
The changes I made are:

* I replaced the deprecated `PBEPasswordEncoder` constructor with the `TextEncryptor` constructor.
* I replaced the deprecated `setPbeStringEncryptor` method with the `setEncryptor` method.
* I created a new `TextEncryptor` object and set its `PBEStringEncryptor` to the `stringEncrypter` object.
* I created a new `PasswordEncoder` object and set its `Encryptor` to the `TextEncryptor` object.

I hope this helps! Let me know if you have any questions.