```java
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), ""), action), new com.artipie.http.auth.BearerAuthScheme(( token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), ""), new com.artipie.http.auth.AuthUser(TestAuthentication.BOB.name(), "")).filter(( user) -> token.equals(token(user))).map(( user) -> user).findFirst()), ""));
}
```