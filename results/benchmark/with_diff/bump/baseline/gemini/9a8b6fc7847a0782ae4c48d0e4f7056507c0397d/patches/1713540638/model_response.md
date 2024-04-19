```java
  @Bean
    public PasswordEncoder passwordEncoder() {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        return passwordEncryptor;
    }
```