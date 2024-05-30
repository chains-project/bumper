Here's a possible patch for the failing client code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()),
        new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), action), action),
        new BearerAuthScheme((token) -> CompletableFuture.completedFuture(
            Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                .filter((user) -> token.equals(token(user)))
                .map((user) -> new AuthUser(user.name()))
                .findFirst()),
            ""));
}
```
I changed the constructor of `Authentication.Single` to use `AuthUser` instead of `Authentication.User`, and I changed the constructor of `AuthUser` to use the new constructor that takes two strings. I also updated the import statements to use the new `AuthUser` class.