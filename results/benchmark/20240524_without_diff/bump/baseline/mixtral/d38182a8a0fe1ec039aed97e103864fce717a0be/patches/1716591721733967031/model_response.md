Here's a fixed version of the method that should resolve the error:

```java
@Override
public Optional<Authentication.User> user() {
    return Optional.ofNullable(new Authentication.User("alice"));
}
```

In this version, I replaced `Optional.of` with `Optional.ofNullable` to avoid a potential `NullPointerException` if the `User` object cannot be created for some reason. This change should not affect the method's behavior if the `User` object is always successfully created.

Note that this change assumes that the `Authentication.User` constructor does not throw any exceptions. If it does, you may need to add additional error handling code to ensure that the method always returns an `Optional<Authentication.User>` object.