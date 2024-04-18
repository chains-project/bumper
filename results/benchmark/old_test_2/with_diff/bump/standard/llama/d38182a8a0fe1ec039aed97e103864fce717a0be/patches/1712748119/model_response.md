Here's a possible patch to fix the error:
```diff
-@java.lang.Override
-public com.artipie.http.Slice slice(final java.lang.String action) {
-    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(TestAuthentication.ALICE.name(), action), new com.artipie.http.auth.BearerAuthScheme((token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new com.artipie.http.auth.Authentication.User(user.name())).findFirst()), ""));
+@java.lang.Override
+public com.artipie.http.Slice slice(final java.lang.String action) {
+    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(com.artipie.http.auth.AuthUser.valueOf(TestAuthentication.ALICE.name()), action), new com.artipie.http.auth.BearerAuthScheme((token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new com.artipie.http.auth.Authentication.User(user.name())).findFirst()), ""));
```
The patch replaces the line `new com.artipie.http.auth.Permissions.Single(TestAuthentication.ALICE.name(), action)` with `new com.artipie.http.auth.Permissions.Single(com.artipie.http.auth.AuthUser.valueOf(TestAuthentication.ALICE.name()), action)`.


The error was caused by the fact that `TestAuthentication.ALICE` is a `java.lang.String`, but the constructor of `com.artipie.http.auth.Permissions.Single` expects a `com.artipie.http.auth.AuthUser` object. The `AuthUser` class has a `valueOf` method that can be used to create an instance of the class from a string, so we call that method to get an instance of `AuthUser` and then pass it to the constructor of `Permissions.Single`.


With this patch, the code should now compile without any errors.