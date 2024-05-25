```java
  @Override
                    public Optional<Authentication.User> user() {
                        Authentication.User user = new Authentication.User("alice");
                        return Optional.ofNullable(user);
                    }
```