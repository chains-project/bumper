```java
  @Bean
    public PasswordEncoder passwordEncoder() {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        passwordEncryptor.setPoolSize("1");
        return passwordEncryptor;
    }
```