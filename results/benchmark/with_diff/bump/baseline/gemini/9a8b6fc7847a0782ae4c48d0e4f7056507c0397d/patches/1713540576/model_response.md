```java
  @Bean
    public PasswordEncoder passwordEncoder() {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        passwordEncryptor.setPasswordEncoder(new PBEWithMD5AndDESCipherTextEncryptor());
        return passwordEncryptor;
    }
```