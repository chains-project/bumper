```java
@java.lang.Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    org.jasypt.encryption.pbe.StandardPBEStringEncryptor encryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
    encryptor.setPassword(this.password);
    encryptor.setAlgorithm(this.algorithm);
    encryptor.setSaltGenerator(this.saltGenerator);
    encryptor.setProviderName(this.providerName);
    encryptor.setIterationCount(this.iterationCount);
    encryptor.setKeyObtentionIterations(this.keyObtentionIterations);
    encryptor.setDigest(this.digest);
    encryptor.setStringOutputType(this.stringOutputType);
    encoder.setPasswordEncryptor(encryptor);
    return encoder;
}
```