```java
  @Override
                    public Optional<Authentication.User> user() {
                        return Optional.of(Authentication.User.of("alice"));
                    }
```