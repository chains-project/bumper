Here's the fixed version of the method:

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
        org.jasypt.util.text.TextEncryptor encryptor = new org.jasypt.util.text.TextEncryptor();
        encryptor.setPbeStringEncryptor(stringEncrypter);
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setTextEncryptor(encryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The changes are:

* Replace `org.jasypt.spring.security.PBEPasswordEncoder` with `org.jasypt.util.text.TextEncryptor`
* Replace `org.jasypt.spring.security.PBEPasswordEncoder` constructor with `org.jasypt.util.text.TextEncryptor` constructor
* Replace `setPbeStringEncryptor` method with `setTextEncryptor` method
* Add `org.jasypt.spring.security.PasswordEncoder` constructor call
* Replace `encodePassword` method call with constructor call
* Replace `isPasswordValid` method call with constructor call.