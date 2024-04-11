Here's the updated method with changes applied to use the new `AuthUser` class:

```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
        .filter(user -> token.equals(token(user)))
        .map(user -> new AuthUser(user.name()))
        .findFirst()), ""));
}
```

In the updated code, I have replaced the usages of `Authentication.User` and `Authentication.Single` with the new `AuthUser` and `Authentication.Single(AuthUser, String)` respectively. Also, I have imported the fully qualified class names for clarity.