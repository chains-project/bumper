Here is a patch that you can apply to the failing client code:
```java
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), ""), action), new com.artipie.http.auth.BearerAuthScheme(( token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter(( user) -> token.equals(token(user))).map(( user) -> new com.artipie.http.auth.AuthUser(user.name(), "")).findFirst()), ""));
}
```
The changes that I made are:

* I replaced `com.artipie.http.auth.Authentication.Single` with `com.artipie.http.auth.Permissions.Single`, which is the new class that should be used to create a single authentication user.
* I replaced `com.artipie.http.auth.Authentication.User` with `com.artipie.http.auth.AuthUser`, which is the new class that should be used to represent an authenticated user.
* I added an empty string as the second argument to the `com.artipie.http.auth.AuthUser` constructor, because the constructor now requires two arguments: a username and an authentication context.

I hope this helps! Let me know if you have any questions.