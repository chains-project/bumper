Here's the updated slice method that uses the new AuthUser class:

```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()),
        new Single(new AuthUser(TestAuthentication.ALICE.name(), action), action),
        new BearerAuthScheme(token -> CompletableFuture.completedFuture(
            Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                .filter(user -> token.equals(token(user)))
                .map(user -> new AuthUser(user.name()))
                .findFirst()),
            ""));
}
```

I created a new `AuthUser` variable for the `Single` constructor to make the code easier to read. Also, I replaced `Authentication.User` with `AuthUser` for the `BearerAuthScheme` constructor.