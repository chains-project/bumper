Here's a fixed version of the `createStringEncoder()` method that should work with the updated library:

```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.encryption.pbe.StandardPBEStringEncryptor stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPasswordEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The changes I made are:

* Replace `org.jasypt.spring.security.PBEPasswordEncoder` with `org.jasypt.spring.security.PasswordEncoder`.
* Replace `org.jasypt.spring.security.PBEPasswordEncoder.PBEPasswordEncoder()` with `org.jasypt.spring.security.PasswordEncoder.PasswordEncoder()`.
* Replace `org.jasypt.spring.security.PBEPasswordEncoder.setPbeStringEncryptor()` with `org.jasypt.spring.security.PasswordEncoder.setPasswordEncryptor()`.
* Remove the unused `encoder.encodePassword()` and `encoder.isPasswordValid()` calls.

These changes should allow the code to compile and run with the updated library.