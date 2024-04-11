Here is a patch that should fix the error:
```java
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), ""), action), new com.artipie.http.auth.BearerAuthScheme(( token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter(( user) -> token.equals(token(user))).map(( user) -> new com.artipie.http.auth.AuthUser(user.name(), "")).findFirst()), ""));
}
```
In this patch, I replaced `TestAuthentication.ALICE.name()` and `TestAuthentication.BOB.name()` with `new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), "")` and `new com.artipie.http.auth.AuthUser(TestAuthentication.BOB.name(), "")` respectively, to match the new constructor signature of `com.artipie.http.auth.AuthUser`.

Additionally, I added an empty string as the second argument to the `AuthUser` constructor, since it now requires two arguments.

I hope this helps! Let me know if you have any questions.