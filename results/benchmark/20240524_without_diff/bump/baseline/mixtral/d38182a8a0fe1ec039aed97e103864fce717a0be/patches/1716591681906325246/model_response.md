Here is a fixed version of the failing method:

```java
@Override
public Optional<Authentication.User> user() {
    return Optional.ofNullable(new Authentication.User("alice"));
}
```

The change made here is to use `Optional.ofNullable` instead of `Optional.of`. This is because `Optional.of` throws a `NullPointerException` if the argument is `null`, whereas `Optional.ofNullable` returns an empty `Optional` if the argument is `null`.

It is possible that the external dependency has been updated to handle `null` values differently, and so the change is necessary to avoid the `NullPointerException`. However, without more context it is difficult to say for sure.

Note that this change does not affect the method signature, and it does not remove the `@Override` decorator. It also does not use any removed library methods, but it does use an added library method (`Optional.ofNullable` was added in Java 8).