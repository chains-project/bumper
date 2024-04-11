Here's the updated code that uses the new `AuthUser` class:

```java
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), ""), action), new com.artipie.http.auth.BearerAuthScheme(( token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter(( user) -> token.equals(token(user))).map(( user) -> new com.artipie.http.auth.AuthUser(user.name(), "")).findFirst()), ""));
}
```

In this updated code, I replaced `com.artipie.http.auth.Authentication.Single` with `com.artipie.http.auth.Permissions.Single` and `com.artipie.http.auth.Authentication.User` with `com.artipie.http.auth.AuthUser`.

The `AuthUser` class has the `name()` method, which can be used to get the user name, so we can just pass an empty string as the second argument to the `AuthUser` constructor.

Note that this code assumes that the `TestAuthentication.ALICE` and `TestAuthentication.BOB` objects have been updated to implement the `com.artipie.http.auth.AuthUser` interface. If not, you may need to update those objects as well.