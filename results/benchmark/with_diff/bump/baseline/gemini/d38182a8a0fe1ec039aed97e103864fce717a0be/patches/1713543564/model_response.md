```java
@Override
public Slice slice(final String action) {
    final AuthUser user = new AuthUser(TestAuthentication.ALICE.name(), "");
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(user, action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(auth -> token.equals(token(auth)))
                    .map(auth -> new AuthUser(auth.name(), ""))
                    .findFirst()
            ),
            ""
        )
    );
}
```