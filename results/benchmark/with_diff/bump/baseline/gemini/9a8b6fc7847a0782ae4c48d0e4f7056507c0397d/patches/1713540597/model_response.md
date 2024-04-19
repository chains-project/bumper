```java
@Bean
    public PasswordEncoder passwordEncoder() {
        PBEStringEncryptor encryptor = new PBEStringEncryptor();
        StringEncryptor passwordEncryptor = new StringEncryptor();
        PBEConfig config = new PBEConfig();
        config.setPassword(encryptorPassword);
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setProviderName("SunJCE");
        config.setIvGeneratorClassName("org.jasypt.iv.RandomIvGenerator");
        config.setStringOutputType("base64");
        encryptor.setConfig(config);
        passwordEncryptor.setAlgorithm("PBEWithMD5AndDES");
        passwordEncryptor.setStringOutputType("base64");
        passwordEncryptor.setPassword(encryptorPassword);
        return passwordEncryptor;
    }
```