```java
  @Bean
    public PasswordEncoder passwordEncoder() {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        passwordEncryptor.setPassword(encryptorPassword);
        return passwordEncryptor;
    }
```