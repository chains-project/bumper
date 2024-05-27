Here's a fixed version of the `createStringEncoder()` method that should work with the updated library version:
```java
@java.lang.Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.encryption.pbe.PBEStringEncryptor encryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
    encryptor.setAlgorithm("PBEWithMD5AndTripleDES");
    encryptor.setPassword("your-encryption-password");

    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(encryptor);
    return encoder;
}
```
In this version, we create an instance of `PBEStringEncryptor` and set its algorithm and password. Then, we create an instance of `PasswordEncoder` and set its password encryptor to the `PBEStringEncryptor` instance we created earlier.

Note that you will need to replace `"your-encryption-password"` with a secure password of your choice.