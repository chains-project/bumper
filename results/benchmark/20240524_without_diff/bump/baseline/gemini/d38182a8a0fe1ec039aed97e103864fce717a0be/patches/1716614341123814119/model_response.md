```java
@Override
                    public Optional<Authentication.User> user() {
                        return Optional.ofNullable(/*++*/new Authentication.User("alice"));
                    }
```