Here is the proposed patch for the failing client code:

```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), action), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new AuthUser(user.name())).findFirst()), ""));
}
```

In this patch, I replaced the usage of `Authentication.User` with `AuthUser` and used the new constructor `AuthUser(String, String)` to create instances of `AuthUser`. I also replaced the usage of `Authentication.Single` with `Authentication.Single(AuthUser, String)` constructor.