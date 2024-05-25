Sure, here's a possible patch for the failing code:
```java
  @Override
  public Optional<Authentication.User> user() {
    Authentication.User user = new Authentication.User("alice");
    return Optional.of(user);
  }
```
This patch creates a variable `user` to store the new `Authentication.User` object and returns it using `Optional.of()`. This should fix the "cannot find symbol" error.