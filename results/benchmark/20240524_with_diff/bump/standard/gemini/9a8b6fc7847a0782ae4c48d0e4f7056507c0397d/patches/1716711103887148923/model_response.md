```java
@org.springframework.context.annotation.Bean
public org.acegisecurity.providers.encoding.PasswordEncoder passwordEncoder() {
    org.jasypt.encryption.pbe.StandardPBEByteEncryptor encryptor = new org.jasypt.encryption.pbe.StandardPBEByteEncryptor();
    encryptor.setPassword(encryptorPassword);
    encryptor.setSaltGenerator(new org.jasypt.salt.RandomSaltGenerator());
    org.jasypt.util.password.StrongPasswordEncryptor passwordEncryptor = new org.jasypt.util.password.StrongPasswordEncryptor();
    passwordEncryptor.setEncryptor(encryptor);
    return passwordEncryptor;
}
```