```java
public Slice slice(final String action) {
    AuthUser user = new AuthUser(TestAuthentication.ALICE.name(), "");
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(user, action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(u -> token.equals(token(u)))
                    .map(u -> new AuthUser(u.name(), ""))
                    .findFirst()
            ),
            ""
        )
    );
}
```